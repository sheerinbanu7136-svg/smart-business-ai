import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Startup Team",
    page_icon="🚀",
    layout="wide"
)

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

menu = st.sidebar.radio(
    "📋 MENU",
    [
        "🏠 Dashboard",
        "🏢 Company Profile",
        "📦 Product Management",
        "📦 Inventory Information",
        "👥 Customer Management",
        "💰 Sales Management",
        "💸 Expense Management",
        "📊 Profit & Loss",
        "🤖 AI Assistant", 
        "📄 Reports", 
        "📋 Tender AI",

    ]
)

# ---------------- DASHBOARD ----------------

if menu == "🏠 Dashboard":

    st.title("🚀 STARTUP TEAM")
    st.subheader("AI Business Management System")

    st.image("image/background.jpg", use_container_width=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Today's Sales", "₹0")

    with col2:
        st.metric("📦 Products", "0")

    with col3:
        st.metric("👥 Customers", "0")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("📦 Stock", "0")

    with col5:
        st.metric("💸 Expenses", "₹0")

    with col6:
        st.metric("📈 Profit", "₹0")


# ---------------- COMPANY PROFILE ----------------

if menu == "🏢 Company Profile":

    st.title("🏢 Company Profile")

    st.image("image/company_profile.jpg", use_container_width=True)

    company = st.text_input("Company Name")
    owner = st.text_input("Owner Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("Save Company"):
        st.success("✅ Company Profile Saved Successfully!")
# ---------------- PRODUCT MANAGEMENT ----------------

if menu == "📦 Product Management":

    st.title("📦 Product Management")

    st.image("image/product.jpg", use_container_width=True)

    product_name = st.text_input("Product Name")
    product_id = st.text_input("Product ID")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0)
    stock = st.number_input("Stock", min_value=0)

    if st.button("Save Product"):
        st.success("✅ Product Saved Successfully!")


# ---------------- INVENTORY INFORMATION ----------------

if menu == "📦 Inventory Information":

    st.title("📦 Inventory Information")

    st.image("image/inventor.jpg", use_container_width=True)

    product_name = st.text_input("Product Name")
    available_stock = st.number_input("Available Stock", min_value=0)
    reorder_level = st.number_input("Reorder Level", min_value=0)
    supplier_name = st.text_input("Supplier Name")

    if st.button("Update Inventory"):
        st.success("✅ Inventory Updated Successfully!")

# ---------------- CUSTOMER MANAGEMENT ----------------

if menu == "👥 Customer Management":

    st.title("👥 Customer Management")

    st.image("image/customer.jpg", use_container_width=True)

    customer_name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("Save Customer"):
        st.success("✅ Customer Saved Successfully!")


# ---------------- SALES MANAGEMENT ----------------

if menu == "💰 Sales Management":

    st.title("💰 Sales Management")

    st.image("image/sales.jpg", use_container_width=True)

    customer_name = st.text_input("Customer Name")
    product_name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=1)
    price = st.number_input("Price", min_value=0)

    total = quantity * price

    st.write(f"### Total Amount : ₹{total}")

    if st.button("Save Sales"):
        st.success("✅ Sales Saved Successfully!")        

# ---------------- EXPENSE MANAGEMENT ----------------

if menu == "💸 Expense Management":

    st.title("💸 Expense Management")

    st.image("image/expense.jpg", use_container_width=True)

    expense_name = st.text_input("Expense Name")
    amount = st.number_input("Amount", min_value=0)
    expense_date = st.date_input("Expense Date")
    description = st.text_area("Description")

    if st.button("Save Expense"):
        st.success("✅ Expense Saved Successfully!")


# ---------------- PROFIT & LOSS ----------------

if menu == "📊 Profit & Loss":

    st.title("📊 Profit & Loss")

    st.image("image/profit.jpg", use_container_width=True)

    total_sales = st.number_input("Total Sales (₹)", min_value=0)
    total_expense = st.number_input("Total Expenses (₹)", min_value=0)

    profit = total_sales - total_expense

    st.write(f"## Profit / Loss : ₹{profit}")

    if profit > 0:
        st.success("✅ Business is in Profit")

    elif profit < 0:
        st.error("❌ Business is in Loss")

    else:
        st.info("⚖️ No Profit, No Loss")

# ---------------- AI ASSISTANT ----------------

if menu == "🤖 AI Assistant":

    st.title("🤖 AI Business Assistant")

    st.image("image/ai_assistant.jpg", use_container_width=True)

    question = st.selectbox(
        "Select your Question",
        [
            "How can I increase sales?",
            "How can I reduce expenses?",
            "How can I improve customer satisfaction?",
            "How can I increase profit?",
            "How can I manage inventory?",
            "How can I attract more customers?",
            "Best marketing ideas?",
            "How can I grow my startup?",
            "How can I improve product quality?",
            "How can I increase online sales?",
            " How much sales should I do today?",
            "How much profit should I earn today?",
            "How should I talk to dealers?",
            "How should I talk to customers?",
            "Which product should I sell more today?",
            "Should I give discounts today?",
            "How much stock should I order today?",
            "What should be today's business target?",
            "How can I increase today's profit?",
            "What should I do first in my business today?",
            "How can I improve customer service?",
            "How can I increase repeat customers?",
            "What is the best marketing strategy for today?",
            "How can I reduce product returns?",
            "How can I improve employee performance?",
            "How can I manage cash flow effectively?",
            "Which product gives the highest profit?",
            " How can I increase monthly sales?",
            "What business mistakes should I avoid today?",
            "What should I focus on to grow my business?"
        ]
    )

    if st.button("Get AI Answer"):

        answers = {
            "How can I increase sales?":
            "Offer discounts, improve marketing, advertise on social media, and provide better customer service.",

            "How can I reduce expenses?":
            "Track daily expenses, reduce waste, and avoid unnecessary spending.",

            "How can I improve customer satisfaction?":
            "Provide quality products, quick delivery, and excellent customer support.",

            "How can I increase profit?":
            "Increase sales, reduce expenses, and improve pricing strategies.",

            "How can I manage inventory?":
            "Monitor stock daily and reorder products before they run out.",

            "How can I attract more customers?":
            "Use digital marketing, referral offers, and social media promotions.",

            "Best marketing ideas?":
            "Use Facebook, Instagram, YouTube, influencer marketing, and festival offers.",

            "How can I grow my startup?":
            "Focus on innovation, customer needs, and continuous improvement.",

            "How can I improve product quality?":
            "Collect customer feedback and maintain strict quality checks.",

            "How can I increase online sales?":
            "Sell through your website and marketplaces, and use online advertising.",

    
           "How can I improve customer service?":
           " Respond quickly, listen carefully to customers, solve their problems, and always be polite.",

           "How can I increase repeat customers?": 
           " Provide quality products, offer loyalty rewards, and maintain regular communication with customers.",

           "What is the best marketing strategy for today?": 
           " Promote your products on social media, run limited-time offers, and share customer reviews.",

           "How can I reduce product returns?": 
           " Check product quality before delivery, provide accurate product details, and pack items safely.",

           "How can I improve employee performance?": 
           " Give clear goals, provide training, appreciate good work, and encourage teamwork.",

           "How can I manage cash flow effectively?": 
           " Track daily income and expenses, collect payments on time, and avoid unnecessary spending.",

           "Which product gives the highest profit?":
             "📈 Focus on products with high demand, good profit margins, and fast sales.",

           "How can I increase monthly sales?": 
           "Increase marketing, introduce special offers, and improve customer relationships.",

           "What business mistakes should I avoid today?": 
           " Avoid unnecessary expenses, poor customer service, overstocking, and late deliveries.",

          "What should I focus on to grow my business?": 
          " Focus on customer satisfaction, product quality, marketing, and consistent business planning."
}
        
        st.success("AI Answer")
        st.write(answers[question])

if menu == "📈 AI Sales Prediction":

    st.title("📈 AI Sales Prediction")
    st.image("image/sales_prediction.jpg", use_container_width=True)

    today_sales = st.number_input("Enter Today's Sales (₹)", min_value=0)

    if st.button("Predict Sales"):

        if today_sales >= 50000:
            st.success("🟢 Excellent! Tomorrow's expected sales: ₹60,000")
            st.info("AI Suggestion: Maintain your current marketing strategy and focus on your best-selling products.")

        elif today_sales >= 30000:
            st.success("🟡 Tomorrow's expected sales: ₹40,000")
            st.info("AI Suggestion: Increase promotions and follow up with existing customers.")

        else:
            st.error("🔴 Tomorrow's expected sales: ₹25,000")
            st.info("AI Suggestion: Offer discounts, advertise on social media, and contact more customers.")

if menu == "📋 Tender AI":

    st.title("📋 Tender AI")

    # Image
    st.image("image/tender.jpg", use_container_width=True)

    tender_name = st.text_input("Tender Name")

    tender_budget = st.number_input(
        "Tender Budget (₹)",
        min_value=0,
        key="tender_budget"
    )

    company_budget = st.number_input(
        "Company Budget (₹)",
        min_value=0,
        key="company_budget"
    )

    if st.button("Check Tender"):

        if company_budget >= tender_budget:
            st.success("✅ You can apply for this tender.")
            st.write("📄 Tender Name:", tender_name)
            st.write("💰 Tender Budget: ₹", tender_budget)
            st.write("🏢 Company Budget: ₹", company_budget)
            st.info("🤖 AI Suggestion: Submit your quotation and apply for the tender.")

        else:
            st.error("❌ Budget is not enough.")
            st.write("📄 Tender Name:", tender_name)
            st.write("💰 Tender Budget: ₹", tender_budget)
            st.write("🏢 Company Budget: ₹", company_budget)
            st.info("🤖 AI Suggestion: Increase your budget or choose another tender.")


if menu == "📄 Reports":

    st.title("📄 Business Reports")

    st.subheader("Available Reports")

    st.write("📊 Daily Sales Report")
    st.write("💰 Profit Report")
    st.write("💸 Expense Report")
    st.write("📦 Inventory Report")
    st.write("👥 Customer Report")

    report = st.selectbox(
        "Select Report",
        [
            "Daily Sales Report",
            "Profit Report",
            "Expense Report",
            "Inventory Report",
            "Customer Report"
        ]
    )

    if st.button("Generate Report"):
        st.success(f"✅ {report} Generated Successfully!")


if menu == "ℹ️ About Us":

    st.title("ℹ️ About Us")

    st.write("🤖 Smart AI Business Management System")

    st.write("This project is developed to help businesses manage:")

    st.write("🏢 Company Profile")
    st.write("📦 Inventory")
    st.write("💰 Sales")
    st.write("📊 Reports")
    st.write("💸 Profit & Loss")
    st.write("🤖 AI Business Assistant")
    st.write("📋 Tender AI")
    st.write("⭐ Customer Feedback")
    st.success("✅ Thank you for using Smart AI Business Management System!")


