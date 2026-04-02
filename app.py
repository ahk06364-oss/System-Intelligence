
import reflex as rx

# --- 1. STATE MANAGEMENT (Logic to keep data safe) ---
class State(rx.State):
    selected_industry: str = ""
    industries: list[str] = [
        "Agricultural", "Airline", "Bank", "Construction", "Diplomacy", 
        "E-Commerce", "Education", "Energy Company", "Food Service", 
        "Healthcare", "Hotel", "Insurance", "Manufacturing", 
        "Military & Defense", "Pharmaceutical", "Real Estate", 
        "Retail Chain", "Shipping Company", "Telecommunication", 
        "Transmission", "Transportation"
    ]

    def set_industry(self, name: str):
        self.selected_industry = name

    def reset_industry(self):
        self.selected_industry = ""

# --- 2. REUSABLE UI COMPONENTS ---
def sidebar_button(label: str, url: str):
    return rx.link(
        rx.button(
            label,
            width="100%",
            variant="outline",
            border_color="#64ffda",
            color="white",
            _hover={"bg": "#64ffda", "color": "#020c1b", "box_shadow": "0 0 15px #64ffda"},
            margin_bottom="10px",
        ),
        href=url,
        is_external=True,
    )

def industry_card(name: str):
    return rx.vstack(
        rx.box(
            rx.text(name, font_size="1.2em", font_weight="bold", color="white"),
            rx.text("NEURAL ENGINE SYNC", font_size="0.7em", color="#64ffda"),
            bg="#112240",
            padding="20px",
            border_radius="15px 15px 0 0",
            border="1px solid #64ffda",
            width="100%",
            text_align="center",
        ),
        rx.button(
            "Access Intelligence Core",
            on_click=lambda: State.set_industry(name),
            width="100%",
            bg="rgba(100, 255, 218, 0.1)",
            color="white",
            border="1px solid #64ffda",
            border_top="none",
            border_radius="0 0 15px 15px",
            _hover={"bg": "white", "color": "#020c1b"},
        ),
        spacing="0",
        width="100%",
    )

# --- 3. MAIN PAGE LAYOUT ---
def index() -> rx.Component:
    return rx.hbox(
        # SIDEBAR
        rx.vstack(
            rx.heading("CORE ENGINE", color="#64ffda", size="md", margin_bottom="20px"),
            sidebar_button("💬 WHATSAPP", "https://wa.me/923245277654"),
            sidebar_button("🌐 WEBSITE", "https://www.ahsanoranalyst.online/"),
            rx.divider(border_color="#64ffda", margin_y="20px"),
            
            rx.cond(
                State.selected_industry != "",
                rx.vstack(
                    rx.heading(f"📂 {State.selected_industry}", size="sm", color="#64ffda"),
                    rx.button("🏠 Exit Dashboard", on_click=State.reset_industry, width="100%", margin_top="10px"),
                    width="100%",
                ),
            ),
            width="280px",
            height="100vh",
            bg="#020c1b",
            padding="20px",
            border_right="2px solid #64ffda",
        ),
        
        # MAIN CONTENT AREA
        rx.box(
            rx.vstack(
                rx.heading("SYSTEM INTELLIGENCE", size="xl", color="#64ffda", margin_bottom="30px"),
                
                # SHOW GRID ONLY IF NO INDUSTRY SELECTED
                rx.cond(
                    State.selected_industry == "",
                    rx.grid(
                        rx.foreach(State.industries, industry_card),
                        columns=[1, 2, 3],
                        spacing="20px",
                        width="100%",
                    ),
                    # SHOW PORTAL IF INDUSTRY SELECTED
                    rx.vstack(
                        rx.heading(f"Welcome to {State.selected_industry} Portal", size="lg"),
                        rx.text("Industrial Modules loading...", color="#64ffda"),
                        padding="50px",
                        bg="#112240",
                        border_radius="15px",
                        border="1px solid #64ffda",
                    )
                ),
                width="100%",
                align_items="center",
            ),
            padding="40px",
            flex="1",
            height="100vh",
            overflow_y="auto",
            bg="radial-gradient(circle at top right, #0a192f, #020c1b)",
        ),
        width="100%",
        height="100vh",
    )

# --- 4. APP INITIALIZATION ---
app = rx.App(
    style={
        "font_family": "Inter",
        "background_color": "#020c1b",
    }
)
app.add_page(index, title="System Intelligence | Ahsan Khan")
