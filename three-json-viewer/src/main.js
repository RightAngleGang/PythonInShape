// src/main.js
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

console.log("Vite + Three OK ✅");

// ---------------------------
// Renderer / Scene / Camera
// ---------------------------
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setClearColor(0x111111);
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.01, 5000);
camera.position.set(8, 8, 14);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Lights
scene.add(new THREE.AmbientLight(0xffffff, 0.6));
const dir = new THREE.DirectionalLight(0xffffff, 0.8);
dir.position.set(10, 20, 10);
scene.add(dir);

// Helpers
scene.add(new THREE.AxesHelper(4));
scene.add(new THREE.GridHelper(50, 50));

// ---------------------------
// Tooltip (hover points)
// ---------------------------
let tooltip = document.getElementById("tooltip");
if (!tooltip) {
  tooltip = document.createElement("div");
  tooltip.id = "tooltip";
  tooltip.style.position = "fixed";
  tooltip.style.pointerEvents = "none";
  tooltip.style.background = "rgba(0,0,0,0.7)";
  tooltip.style.color = "white";
  tooltip.style.padding = "4px 8px";
  tooltip.style.borderRadius = "6px";
  tooltip.style.fontSize = "12px";
  tooltip.style.fontFamily = "system-ui";
  tooltip.style.display = "none";
  document.body.appendChild(tooltip);
}

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let lastMouseClientX = 0;
let lastMouseClientY = 0;
window.addEventListener("mousemove", (e) => {
  lastMouseClientX = e.clientX;
  lastMouseClientY = e.clientY;
  mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
});

// ---------------------------
// Load JSON
// ---------------------------
const res = await fetch("/data.json");
if (!res.ok) throw new Error(`data.json introuvable: ${res.status} ${res.statusText}`);
const data = await res.json();
console.log("data.json chargé ✅", data);

// Map name -> Vector3
const pointsByName = new Map();
for (const p of data.points) {
  pointsByName.set(p.name, new THREE.Vector3(p.x, p.y, p.z));
}

function getPoint(name) {
  const v = pointsByName.get(name);
  if (!v) throw new Error(`Point introuvable: ${name}`);
  return v.clone();
}

// ---------------------------
// Materials (simple)
// ---------------------------
const matPoint = new THREE.MeshStandardMaterial({ color: 0xff5555 });
const matSolid = new THREE.MeshStandardMaterial({
  color: 0x4aa3ff,
  transparent: true,
  opacity: 0.35,
  side: THREE.DoubleSide,
});
const matLine = new THREE.LineBasicMaterial({ color: 0x00ffff });

// ---------------------------
// Draw points
// ---------------------------
const spherePt = new THREE.SphereGeometry(0.08, 16, 16);
const pointMeshes = [];

for (const [name, v] of pointsByName.entries()) {
  const m = new THREE.Mesh(spherePt, matPoint);
  m.position.copy(v);
  m.userData = { name };
  scene.add(m);
  pointMeshes.push(m);
}

// ---------------------------
// Geometry helpers
// ---------------------------
function addPolyline(vecs, closed = false) {
  const pts = closed ? [...vecs, vecs[0]] : vecs;
  const geom = new THREE.BufferGeometry().setFromPoints(pts);
  const line = new THREE.Line(geom, matLine);
  scene.add(line);
  return line;
}

function addEdges(mesh) {
  const edges = new THREE.EdgesGeometry(mesh.geometry, 1e-6);
  const e = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: 0xffffff }));
  e.position.copy(mesh.position);
  e.quaternion.copy(mesh.quaternion);
  e.scale.copy(mesh.scale);
  scene.add(e);
  return e;
}

function addIndexedMesh(vertices /* Vector3[] */, indices /* number[] */) {
  const positions = new Float32Array(vertices.length * 3);
  vertices.forEach((v, i) => {
    positions[i * 3 + 0] = v.x;
    positions[i * 3 + 1] = v.y;
    positions[i * 3 + 2] = v.z;
  });

  const geom = new THREE.BufferGeometry();
  geom.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  geom.setIndex(indices);
  geom.computeVertexNormals();

  const mesh = new THREE.Mesh(geom, matSolid);
  scene.add(mesh);
  addEdges(mesh);
  return mesh;
}

// Triangulate a planar polygon in 3D (best effort). If fails -> null
function triangulatePlanarPolygon3D(points3D) {
  if (points3D.length < 3) return null;

  // Find a non-degenerate normal using first non-collinear triple
  let n = null;
  let iA = 0, iB = 1, iC = 2;
  for (let i = 0; i < points3D.length - 2 && !n; i++) {
    for (let j = i + 1; j < points3D.length - 1 && !n; j++) {
      for (let k = j + 1; k < points3D.length && !n; k++) {
        const a = points3D[i], b = points3D[j], c = points3D[k];
        const ab = b.clone().sub(a);
        const ac = c.clone().sub(a);
        const nn = ab.clone().cross(ac);
        if (nn.lengthSq() > 1e-10) {
          n = nn.normalize();
          iA = i; iB = j; iC = k;
        }
      }
    }
  }
  if (!n) return null; // all points collinear

  // Build local basis (u, v) on the polygon plane
  const origin = points3D[iA].clone();
  const u = points3D[iB].clone().sub(origin).normalize();
  const v = n.clone().cross(u).normalize();

  // Project to 2D
  const pts2 = points3D.map((p) => {
    const d = p.clone().sub(origin);
    return new THREE.Vector2(d.dot(u), d.dot(v));
  });

  // Triangulate in 2D
  const tris = THREE.ShapeUtils.triangulateShape(pts2, []);
  if (!tris || tris.length === 0) return null;

  // Convert triangulation to indices
  const indices = [];
  for (const t of tris) {
    indices.push(t[0], t[1], t[2]);
  }
  return { vertices: points3D, indices };
}

// ---------------------------
// Special shape renderers
// ---------------------------
function renderCubeOrPave(points8) {
  // Convention: [0..3] bottom loop, [4..7] top loop
  if (points8.length !== 8) return false;

  const idx = [];
  const quad = (a, b, c, d) => {
    idx.push(a, b, c, a, c, d);
  };

  // bottom (0,1,2,3) + top (4,5,6,7)
  quad(0, 1, 2, 3);
  quad(4, 5, 6, 7);

  // sides
  quad(0, 1, 5, 4);
  quad(1, 2, 6, 5);
  quad(2, 3, 7, 6);
  quad(3, 0, 4, 7);

  addIndexedMesh(points8, idx);
  return true;
}

function renderPyramid(points5) {
  // Convention: base 4 points + apex last
  if (points5.length !== 5) return false;

  const base = points5.slice(0, 4);
  const apex = points5[4];

  const vertices = [...base, apex]; // 0..3 base, 4 apex
  const idx = [];
  const tri = (a, b, c) => idx.push(a, b, c);

  // base (two triangles)
  tri(0, 1, 2);
  tri(0, 2, 3);

  // sides
  tri(0, 1, 4);
  tri(1, 2, 4);
  tri(2, 3, 4);
  tri(3, 0, 4);

  addIndexedMesh(vertices, idx);
  return true;
}

function renderPlanarPolygonFace(pointsN) {
  const tri = triangulatePlanarPolygon3D(pointsN);
  if (!tri) return false;
  addIndexedMesh(tri.vertices, tri.indices);
  return true;
}

function renderSegment(p2) {
  if (p2.length !== 2) return false;
  addPolyline(p2, false);
  return true;
}

function renderSphere(center, radius) {
  const geom = new THREE.SphereGeometry(radius, 32, 16);
  const mesh = new THREE.Mesh(geom, matSolid);
  mesh.position.copy(center);
  scene.add(mesh);
  addEdges(mesh);
}

function renderCone(baseCenter, radius, apex) {
  const height = apex.distanceTo(baseCenter);
  if (height <= 1e-8) return;

  // ConeGeometry is centered at origin along Y; we orient & position it.
  const geom = new THREE.ConeGeometry(radius, height, 32, 1, false);
  const mesh = new THREE.Mesh(geom, matSolid);

  // Direction from base -> apex
  const dirVec = apex.clone().sub(baseCenter).normalize();

  // Rotate cone's +Y axis onto dirVec
  const q = new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 1, 0), dirVec);
  mesh.quaternion.copy(q);

  // Place at midpoint between base and apex (because geometry centered)
  const mid = baseCenter.clone().add(apex).multiplyScalar(0.5);
  mesh.position.copy(mid);

  scene.add(mesh);
  addEdges(mesh);

  // Optional: draw axis line
  addPolyline([baseCenter, apex], false);
}

function renderCircle(center, radius, normal) {
  const segments = 64;
  const geom = new THREE.CircleGeometry(radius, segments);
  const mesh = new THREE.Mesh(geom, matSolid);

  // Orient circle: default normal is +Z
  const n = new THREE.Vector3(normal.x, normal.y, normal.z);
  if (n.lengthSq() < 1e-10) n.set(0, 0, 1);
  n.normalize();

  const q = new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 0, 1), n);
  mesh.quaternion.copy(q);
  mesh.position.copy(center);

  scene.add(mesh);

  // Outline
  const ringPts = [];
  for (let i = 0; i < segments; i++) {
    const a = (i / segments) * Math.PI * 2;
    ringPts.push(new THREE.Vector3(Math.cos(a) * radius, Math.sin(a) * radius, 0));
  }
  // rotate + translate ring points
  ringPts.forEach((p) => p.applyQuaternion(q).add(center));
  addPolyline(ringPts, true);
}

// ---------------------------
// Render shapes with special cases
// ---------------------------
for (const s of data.shapes) {
  try {
    if (s.type === "Polygon") {
      const pts = (s.points || []).map(getPoint);

      // Predefined solids: faces
      if (s.subtype === "Cube" && pts.length === 8) {
        renderCubeOrPave(pts);
        continue;
      }
      if ((s.subtype === "Pavé" || s.subtype === "Pave" || s.subtype === "Pavé droit") && pts.length === 8) {
        renderCubeOrPave(pts);
        continue;
      }
      if (s.subtype === "Pyramide" && pts.length === 5) {
        renderPyramid(pts);
        continue;
      }

      // Predefined planar faces
      if (["Carré", "Carre", "Rectangle", "Triangle"].includes(s.subtype) && pts.length >= 3) {
        // si triangle dégénéré (collinear), triangulation échoue => fallback polyline
        if (renderPlanarPolygonFace(pts)) {
          // outline too
          addPolyline(pts, true);
          continue;
        }
        // fallback
        addPolyline(pts, pts.length > 2);
        continue;
      }

      // Segment
      if (s.subtype === "Segment" && pts.length === 2) {
        renderSegment(pts);
        continue;
      }

      // Unknown polygon subtype: draw lines in provided order
      addPolyline(pts, pts.length >= 3);
      continue;
    }

    if (s.type === "Sphere") {
      const c = getPoint(s.center);
      renderSphere(c, Number(s.radius) || 1);
      continue;
    }

    if (s.type === "Cone") {
      const base = getPoint(s.center);
      const apex = getPoint(s.apex);
      renderCone(base, Number(s.radius) || 1, apex);
      continue;
    }

    if (s.type === "Circle") {
      const c = getPoint(s.center);
      renderCircle(c, Number(s.radius) || 1, s.normal || { x: 0, y: 0, z: 1 });
      continue;
    }

    // Unknown type: ignore (or log)
    console.warn("Type non géré:", s.type, s);
  } catch (e) {
    console.error("Erreur rendu shape:", s?.name, e);
  }
}

// ---------------------------
// Auto-center camera on content
// ---------------------------
const box = new THREE.Box3().setFromObject(scene);
const center = box.getCenter(new THREE.Vector3());
const size = box.getSize(new THREE.Vector3()).length();

controls.target.copy(center);
camera.position.copy(center).add(new THREE.Vector3(size * 0.6, size * 0.4, size * 0.7));
camera.near = Math.max(0.01, size / 1000);
camera.far = Math.max(200, size * 10);
camera.updateProjectionMatrix();

// Resize
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// ---------------------------
// Render loop (+ hover tooltip)
// ---------------------------
function animate() {
  controls.update();

  raycaster.setFromCamera(mouse, camera);
  const hits = raycaster.intersectObjects(pointMeshes, false);

  if (hits.length > 0) {
    const obj = hits[0].object;
    tooltip.style.display = "block";
    tooltip.textContent = obj.userData.name;
    tooltip.style.left = `${lastMouseClientX + 10}px`;
    tooltip.style.top = `${lastMouseClientY + 10}px`;
  } else {
    tooltip.style.display = "none";
  }

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}

animate();
