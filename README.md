# Terminal Commander: A Python CLI To-Do App

### **By George Freedom**

This repository contains a terminal-based to-do application built in Python. Think of it not just as an app, but as a foundational blueprint or a mission-critical prototype for a larger system.
Its primary purpose is not to be a feature-complete product for daily use, but to serve as a clear case study in architecting resilient software, demonstrating several key concepts.

--

## 🚀 Key Features
* **SOLID Design:** Strict adherence to OOP principles for a scalable, robust core.

* **AI-Assisted Workflow:** Simulation of high-velocity, modern development cycles.

* **CSV Persistence:** Lightweight, automated data storage via localized .csv files.

* **Tactical CLI:** Clean, distraction-free command-line interface for all operations.

* **Decoupled Logic:** Deliberate separation of concerns for maximum maintainability.

--

## ⚙️ System Architecture
A 3-tier modular structure enforcing strict boundaries between interaction and data.

### 🖥️ Presentation (CLI)
* **Terminal-based** interface for user input and visual status readouts.

* Integrated **Mermaid** blueprints for system logic visualization.

### 🧠 Logic (Service)
* Central engine enforcing business rules and **SOLID** architectural patterns.

* Acts as the primary bridge, keeping logic decoupled from I/O.

### 📁 Data (Repository)
* Manages physical **CSV** I/O and automated file generation.

* Encapsulates storage format to allow seamless backend transitions.

--

### System Diagram
```mermaid
graph TD;
    subgraph "Presentation Layer"
        A[CommandLineUI];
    end

    subgraph "Business Logic Layer"
        B{TaskManager};
    end

    subgraph "Data Access Layer"
        C[CsvDatabase];
    end
    
    subgraph "Data Models"
        D[Task];
    end
    
    subgraph "Physical Storage"
        E[(tasks.csv)];
    end

    A -- "Uses / Invokes" --> B;
    B -- "Manages / Creates" --> D;
    B -- "Depends on" --> C;
    C -- "Accesses" --> E;
```


## File Structure
```
app/
│
├── commander_db/
│   └── to_do_list.csv
├── main.py
├── ui.py
├── task_manager.py
├── database.py
├── models.py
├── config.py
│
├── README.md
└── LICENSE.md
```


## 💡 Development Philosophy & AI Collaboration

This project was built to test a modern, AI-assisted workflow. My contribution was the architectural design and final quality assurance: I defined the requirements and SOLID principles, guided the AI's implementation, and then performed all code reviews and testing. This approach shifts the developer's value from writing code to designing systems and guaranteeing the result.


## 📖 Context & Further Reading

This project and the experience of building it served as the primary catalyst for my article on the evolving role of developers in the AI era. If you are interested in the deeper strategic implications of this workflow, you can read the full article on my website:

* **[Basic Training is Over: The New Role of Developers in the AI War Room](https://georgefreedom.com/basic-training-is-over-the-new-role-of-developers-in-the-ai-war-room/)**


## ⚙️ How to Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/GeorgeFreedomTech/terminal-commander.git
    cd terminal-commander
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
3.  **Run the Application:**
    *This project uses only standard Python libraries, so no `requirements.txt` is needed for this basic version.*
    ```bash
    python main.py
    ```
4.  Follow the on-screen instructions in your terminal.


## 🔗 Let's Connect:

* Visit my website: **[https://GeorgeFreedom.com](https://GeorgeFreedom.com)**
* Connect on LinkedIn: **[https://www.linkedin.com/in/georgefreedom/](https://www.linkedin.com/in/georgefreedom/)**
* Let's talk: **[https://cal.com/georgefreedom](https://cal.com/georgefreedom)**


## 📜 License:

Copyright (c) 2025 Jiří Svoboda (George Freedom) / George Freedom Tech

This project is licensed under:
* Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

---

We build for the Future!
