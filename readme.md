# Connect 🎓🚗🏠

> **Beyond the Campus.** A community-driven mobile platform connecting university students to solve the housing bureaucracy and daily commuting challenges through smart, peer-to-peer sharing.

### 💡 About the Project
**Connect** is an academic extension project designed to modernize how students handle their logistical and socio-economic barriers. Its mission is to reduce evasion rates by optimizing the academic community's own resources—matching those who need a ride or a room with those who can offer it.

This project implements a **Clean Architecture Monorepo**, separating a robust containerized Python/Django API from a cross-platform React Native mobile client, prioritizing performance, scalability, and strict security validations.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django REST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![React Native](https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)

### 🧩 The Problem vs. The Solution

#### 1. The Commuting Trap (High Costs)
* **The Catch:** **Financial Strain**. Students rely on expensive intercity transport or private vans, which can cost up to R$ 500.00 monthly, severely impacting middle-to-low-income families.
* **The Smart Carpooling Win:** An integrated map system (Uber/99 style) connects users based on common routes (Home-University-Work), allowing students to split fuel costs dynamically.

#### 2. The Housing Barrier (Bureaucracy)
* **The Catch:** Real estate agencies demand guarantors, proof of income, and high security deposits, making the relocation process chaotic for students from other cities.
* **The Peer-to-Peer Win:** A customized bulletin board where students can list and filter specific accommodations (kitnets, shared rooms, republics) by gender, type, and proximity to the campus—cutting out the middleman.

#### 3. The Trust Issue
* **The Catch:** Open WhatsApp or Facebook groups expose students to scams, harassment, and external threats.
* **The Institutional Auth Win:** The platform features a strict entry barrier. Login and account creation are exclusively validated via the institutional academic email (`@aluno.ifsp.edu.br` or equivalent), creating a verifiable "walled garden".

---

### 🖥️ Architecture Flow

The system operates in a decoupled pipeline designed for rapid development and UX:

| Stage | Component | Description |
| :--- | :--- | :--- |
| **1. Storage** | `Docker + PostgreSQL` | A persistent volume holding the relational data, user profiles, and geolocation coordinates. |
| **2. Backend API** | `Django + DRF` | The core engine handling business logic, authentication middlewares, and CRUD operations. |
| **3. Documentation**| `drf-spectacular` | Auto-generated OpenAPI/Swagger schemas for seamless Front-to-Back contract integration. |
| **4. Client App** | `React Native (Expo)` | The cross-platform mobile application delivering a native feel for both iOS and Android users. |

### 📊 Capability Showcase

**Searching for a Room:**
> *User filters for "Female-only Republics" within "2km" of the campus.*
> The API returns a serialized JSON list of available spots, rendering a clean UI card with photos, rent share, and an internal chat button to negotiate directly with the poster.

---

### 🚀 How to Run

1. **Clone the repository**
```bash
git clone [https://github.com/your-username/campushare.git](https://github.com/your-username/campushare.git)
cd campushare
```

2. **Environment Setup**

Copy ```.env.example``` to ```.env``` and set your local database credentials.

Copy ```frontend/.env.example``` to ```frontend/.env``` and set EXPO_PUBLIC_API_URL to your machine's local IP address (e.g., http://192.168.1.X:8000).

3. **Start the Infrastructure (VS Code Tasks)**
This project includes automated VS Code tasks for a frictionless developer experience. And it's expect you to have already downloaded and installed node, npm, expo and docker.

- Open the Run Task menu (Ctrl+Shift+P -> Tasks: Run Task).

- Run 🚀 1. Iniciar Infra (Docker Debug Mode) to spin up the PostgreSQL and Django containers.

- Run 🔄 4. Django: Migrate to build the database schema.

4. **Start the Mobile Client**
Open a new terminal session in the frontend directory:
```bash
cd frontend
npm install
npx expo start
```
- Web: Press w to open in your browser.

- Mobile: Scan the QR code using the Expo Go app on your device (ensure both are on the same Wi-Fi network).

---

Developed by: @nathanhgo