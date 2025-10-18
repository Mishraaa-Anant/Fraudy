import streamlit as st
from datetime import datetime, timedelta
from typing import List, Dict
import random

# === AHIDS: Autonomous Health Information Defense System ===
# Multi-agent AI system for proactive health misinformation defense

st.set_page_config(
    page_title="AHIDS - Health Defense System",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            padding: 20px;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #00d4aa;
        }
        .high-severity {
            background-color: #ffe0e0;
            border-left-color: #ff4444;
        }
        .medium-severity {
            background-color: #fff3e0;
            border-left-color: #ffaa00;
        }
        .low-severity {
            background-color: #e0f2f1;
            border-left-color: #00ccff;
        }
    </style>
""", unsafe_allow_html=True)

# ========================
# Sample Data & Config
# ========================

misinformation_samples = [
    {
        "text": "Drinking hot water kills COVID instantly.",
        "origin": "fringe_forum_covid_truth",
        "author": "health_rebel_99",
        "platform": "Telegram",
        "timestamp": datetime.now() - timedelta(hours=2)
    },
    {
        "text": "Vaccines cause infertility in young adults.",
        "origin": "anti_vax_collective",
        "author": "natural_immunity_advocate",
        "platform": "Facebook",
        "timestamp": datetime.now() - timedelta(hours=5)
    },
    {
        "text": "5G towers spread coronavirus through radiation.",
        "origin": "conspiracy_theory_hub",
        "author": "5g_awareness_committee",
        "platform": "Twitter",
        "timestamp": datetime.now() - timedelta(hours=1)
    },
    {
        "text": "Bleach mixed with lemon can disinfect your throat.",
        "origin": "fake_remedy_network",
        "author": "wellness_guru_88",
        "platform": "Instagram",
        "timestamp": datetime.now() - timedelta(hours=3)
    },
    {
        "text": "WHO confirms coffee prevents infection.",
        "origin": "misinformation_farm_001",
        "author": "bot_account_fake",
        "platform": "Reddit",
        "timestamp": datetime.now() - timedelta(hours=4)
    },
]

keyword_severity = {
    "high": ["bleach", "5g", "hoax", "infertility", "poison", "deadly", "cover-up"],
    "medium": ["garlic", "coffee", "hot water", "mask", "cure", "instant", "prevents"],
    "low": ["vaccine", "covid", "virus", "immunity", "infection", "health"]
}

keywords_to_responses = {
    "bleach": "Ingesting bleach is extremely dangerous and can cause death. Contact poison control immediately.",
    "infertility": "Vaccines do not cause infertility. Multiple large-scale studies confirm no link between vaccines and reproductive harm.",
    "5g": "5G radio waves cannot spread viruses. COVID-19 is a biological pathogen spread through respiratory droplets.",
    "hoax": "COVID-19 is real and has caused millions of deaths. Refer to WHO, CDC, and peer-reviewed research.",
    "instant cure": "No single substance instantly cures complex diseases. Always consult healthcare providers for treatment.",
    "coffee prevents": "Coffee has no proven preventive properties against infectious diseases. Vaccination and hygiene are evidence-based protection."
}

institutional_data = {
    "City General Hospital": {
        "recent_attacks": 42,
        "false_claims": [
            "City General Hospital is hiding COVID deaths",
            "Doctors at City General are forcing vaccines on patients",
            "City General Hospital profits from unnecessary procedures"
        ]
    },
    "State Health Department": {
        "recent_attacks": 28,
        "false_claims": [
            "State Health Department is tracking citizens through vaccines",
            "Public health officials are suppressing natural remedies",
            "State Health coordinated with pharma to hide vaccine side effects"
        ]
    }
}

# ========================
# Agent 1: Tracker Core
# ========================

class TrackerCore:
    """Epidemiological Intelligence - Detects and maps misinformation spread"""
    
    @staticmethod
    def detect_misinformation(post: str) -> Dict:
        """Early Detection: Identify health misinformation narratives"""
        text = post.lower()
        found_keywords = []
        severity_score = 0
        
        for keyword in keyword_severity["high"]:
            if keyword in text:
                found_keywords.append(keyword)
                severity_score += 3
        
        for keyword in keyword_severity["medium"]:
            if keyword in text:
                found_keywords.append(keyword)
                severity_score += 1.5
        
        for keyword in keyword_severity["low"]:
            if keyword in text:
                found_keywords.append(keyword)
                severity_score += 0.5
        
        if severity_score >= 3:
            severity = "High"
            confidence = min(0.95, 0.5 + (severity_score * 0.1))
        elif severity_score >= 1.5:
            severity = "Medium"
            confidence = min(0.85, 0.4 + (severity_score * 0.1))
        else:
            severity = "Low"
            confidence = min(0.75, 0.3 + (severity_score * 0.1))
        
        return {
            "text": post,
            "severity": severity,
            "confidence": round(confidence, 2),
            "risk_keywords": list(set(found_keywords)),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def map_spread_network(rumor_text: str) -> Dict:
        """Source & Spread Mapping: Create real-time network graph of rumor propagation"""
        rumor_id = f"rumor_{random.randint(1000, 9999)}"
        
        spread_data = {
            "Twitter": {"posts": random.randint(50, 200), "retweets": random.randint(500, 2000)},
            "Facebook": {"posts": random.randint(30, 150), "shares": random.randint(300, 1500)},
            "Telegram": {"messages": random.randint(20, 100), "channels": random.randint(5, 20)},
            "Reddit": {"posts": random.randint(10, 50), "upvotes": random.randint(100, 500)},
            "TikTok": {"videos": random.randint(5, 30), "views": random.randint(1000, 100000)}
        }
        
        super_spreaders = [
            {
                "account": f"influencer_{random.randint(100, 999)}",
                "platform": random.choice(["Twitter", "Facebook", "TikTok"]),
                "followers": random.randint(10000, 500000),
                "amplification_factor": round(random.uniform(1.5, 5.0), 2)
            }
            for _ in range(random.randint(3, 7))
        ]
        
        total_reach = sum(
            v.get("retweets", 0) + v.get("shares", 0) + v.get("messages", 0) + 
            v.get("upvotes", 0) + v.get("views", 0)
            for v in spread_data.values()
        )
        
        return {
            "rumor_id": rumor_id,
            "origin": "fringe_forum_detected",
            "rumor_text": rumor_text,
            "first_detected": (datetime.now() - timedelta(hours=random.randint(1, 24))).isoformat(),
            "spread_data": spread_data,
            "super_spreaders": super_spreaders,
            "total_reach": total_reach
        }

# ========================
# Agent 2: Community Sentinel
# ========================

class CommunitySentinel:
    """Public Intervention - Deploys localized interventions in high-risk forums"""
    
    @staticmethod
    def generate_intervention(claim: str, severity: str) -> Dict:
        """Proactive Correction: Generate context-aware, non-confrontational response"""
        post_id = f"post_{random.randint(10000, 99999)}"
        
        if severity == "High":
            intervention_type = "Urgent_Health_Alert"
            priority_level = "CRITICAL"
        elif severity == "Medium":
            intervention_type = "Fact_Check_Response"
            priority_level = "HIGH"
        else:
            intervention_type = "Informational_Comment"
            priority_level = "MEDIUM"
        
        responses_templates = {
            "bleach": "I understand you're looking for solutions, but bleach is toxic to humans. Safe alternatives include hand hygiene and consulting healthcare providers.",
            "infertility": "This claim circulates often, but major health organizations (CDC, WHO, AMA) have found no evidence linking vaccines to infertility.",
            "5g": "5G uses radio waves at frequencies that cannot infect cells or spread viruses. COVID spreads through respiratory droplets.",
            "hoax": "COVID-19 has caused real illness and death. The best protection is vaccination and evidence-based health measures.",
            "vaccine": "Vaccines have undergone rigorous safety testing. Millions have been vaccinated safely. Speak with your doctor about your specific concerns."
        }
        
        response = responses_templates.get(
            next((k for k in responses_templates if k in claim.lower()), "vaccine"),
            "Please consult trusted health authorities like CDC or WHO for health information."
        )
        
        credible_sources = [
            "WHO (World Health Organization)",
            "CDC (Centers for Disease Control)",
            "Mayo Clinic",
            "National Institutes of Health (NIH)",
            "Peer-reviewed medical journals"
        ]
        
        return {
            "post_id": post_id,
            "original_claim": claim,
            "intervention_type": intervention_type,
            "response": response,
            "credible_sources": credible_sources,
            "priority_level": priority_level
        }
    
    @staticmethod
    def prioritize_interventions(posts: List[str]) -> List[Dict]:
        """Harm Reduction: Prioritize dangerous advice before less critical falsehoods"""
        interventions = []
        
        for claim in posts:
            detection = TrackerCore.detect_misinformation(claim)
            intervention = CommunitySentinel.generate_intervention(claim, detection["severity"])
            interventions.append(intervention)
        
        priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}
        interventions.sort(key=lambda x: priority_order.get(x["priority_level"], 3))
        
        return interventions

# ========================
# Agent 3: Institutional Shield
# ========================

class InstitutionalShield:
    """Provider Defense - Protects healthcare institutions from coordinated attacks"""
    
    @staticmethod
    def monitor_threats(institution: str) -> List[Dict]:
        """Targeted Threat Monitoring: Detect coordinated misinformation campaigns"""
        threats = []
        
        if institution in institutional_data:
            institution_info = institutional_data[institution]
            false_claims = institution_info["false_claims"]
            
            for claim in false_claims:
                threat_types = ["Bot Attack", "Coordinated Campaign", "Defamatory Content", "Conspiracy Theory"]
                threat_type = random.choice(threat_types)
                
                threat = {
                    "threat_id": f"threat_{random.randint(10000, 99999)}",
                    "target_institution": institution,
                    "claim": claim,
                    "reach": random.randint(500, 50000),
                    "origin": random.choice(["fringe_forum", "anti_vax_network", "conspiracy_hub", "coordinated_bot_farm"]),
                    "threat_type": threat_type,
                    "severity": random.choice(["High", "Medium"]),
                    "coordinated_accounts": [f"bot_account_{i}" for i in range(random.randint(2, 8))]
                }
                threats.append(threat)
        
        return threats
    
    @staticmethod
    def generate_counter_statement(institution: str, threat: Dict) -> Dict:
        """Automated Response Protocol: Generate evidence-based counter-statement"""
        
        counter_responses = {
            "hiding": f"{institution} maintains transparent reporting in compliance with healthcare regulations and public health guidelines.",
            "forcing": f"{institution} respects patient autonomy and informed consent. Medical decisions are made collaboratively with patients.",
            "profits": f"{institution}'s mission is patient care. All procedures follow evidence-based medical standards, not profit incentives.",
            "tracking": f"{institution} complies with HIPAA privacy laws. Patient data is protected and used only for healthcare purposes.",
            "suppressing": f"{institution} promotes evidence-based medicine. Natural remedies are discussed when medically appropriate.",
            "hiding vaccine": f"{institution} reports all safety data transparently. Vaccine monitoring systems track safety continuously."
        }
        
        response = counter_responses.get(
            next((k for k in counter_responses if k in threat["claim"].lower()), "hiding"),
            f"{institution} is committed to transparent, evidence-based healthcare and public health protection."
        )
        
        return {
            "institution": institution,
            "threat_summary": f"Threat ID: {threat['threat_id']} | Type: {threat['threat_type']} | Reach: {threat['reach']:,} people",
            "evidence_based_response": response,
            "sources": [
                "HIPAA Compliance Documentation",
                "Medical Ethics Board Records",
                "Peer-reviewed Research",
                "Regulatory Compliance Reports",
                "Patient Testimony & Reviews"
            ],
            "suggested_channels": ["Official Website", "Social Media", "Press Release", "Email Newsletter", "Staff Communication"]
        }

# ========================
# Streamlit UI
# ========================

st.markdown("# ⚔️ AHIDS")
st.markdown("### Autonomous Health Information Defense System")
st.markdown("Multi-Agent AI for Proactive Infodemic Defense")

st.success("✓ System Active - 3 Agents Online")

# Sidebar navigation
st.sidebar.markdown("## Navigation")
page = st.sidebar.radio("Select Agent", [
    "Full Demo",
    "Tracker Core",
    "Community Sentinel",
    "Institutional Shield"
])

# ========================
# FULL DEMO PAGE
# ========================

if page == "Full Demo":
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    if st.button("Run Full System Demo", use_container_width=True, key="demo_btn"):
        with st.spinner("Analyzing health misinformation threats..."):
            # Tracker Core
            detections = [TrackerCore.detect_misinformation(m["text"]) for m in misinformation_samples]
            
            # Community Sentinel
            interventions = CommunitySentinel.prioritize_interventions([m["text"] for m in misinformation_samples])
            
            # Institutional Shield
            shield_threats = InstitutionalShield.monitor_threats("City General Hospital")
            counter_statement = InstitutionalShield.generate_counter_statement(
                "City General Hospital", 
                shield_threats[0]
            ) if shield_threats else None
            
            st.markdown("---")
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Posts Analyzed", len(detections))
            with col2:
                high_risk = sum(1 for d in detections if d["severity"] == "High")
                st.metric("High Risk Posts", high_risk)
            with col3:
                st.metric("Interventions", len(interventions))
            with col4:
                st.metric("Threats Detected", len(shield_threats))
            
            st.markdown("---")
            
            # Tracker Core Results
            st.markdown("## 📡 TRACKER CORE - Early Detection")
            for detection in detections[:3]:
                severity_color = "🔴" if detection["severity"] == "High" else "🟠" if detection["severity"] == "Medium" else "🟢"
                with st.expander(f"{severity_color} {detection['severity']} Severity - {detection['text'][:60]}..."):
                    st.write(f"**Claim:** {detection['text']}")
                    st.write(f"**Severity:** {detection['severity']}")
                    st.write(f"**Confidence:** {detection['confidence']*100:.0f}%")
                    if detection['risk_keywords']:
                        st.write(f"**Risk Keywords:** {', '.join(detection['risk_keywords'])}")
            
            st.markdown("---")
            
            # Community Sentinel Results
            st.markdown("## 🛡️ COMMUNITY SENTINEL - Interventions")
            for intervention in interventions[:2]:
                with st.expander(f"🔧 {intervention['priority_level']} Priority - {intervention['original_claim'][:60]}..."):
                    st.write(f"**Original Claim:** {intervention['original_claim']}")
                    st.write(f"**Priority:** {intervention['priority_level']}")
                    st.info(f"**Intervention:** {intervention['response']}")
                    st.write(f"**Credible Sources:** {', '.join(intervention['credible_sources'])}")
            
            st.markdown("---")
            
            # Institutional Shield Results
            if shield_threats:
                st.markdown("## 🏥 INSTITUTIONAL SHIELD - Defense")
                threat = shield_threats[0]
                with st.expander(f"⚠️ Threat: {threat['threat_type']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Target:** {threat['target_institution']}")
                        st.write(f"**Type:** {threat['threat_type']}")
                        st.write(f"**Reach:** {threat['reach']:,} people")
                    with col2:
                        st.write(f"**False Claim:** {threat['claim']}")
                        st.write(f"**Origin:** {threat['origin']}")
                        st.write(f"**Severity:** {threat['severity']}")
                
                if counter_statement:
                    with st.expander("📋 Generated Counter-Statement"):
                        st.info(counter_statement['evidence_based_response'])
                        st.write(f"**Sources:** {', '.join(counter_statement['sources'])}")
                        st.write(f"**Deploy Via:** {', '.join(counter_statement['suggested_channels'])}")

# ========================
# TRACKER CORE PAGE
# ========================

elif page == "Tracker Core":
    st.markdown("---")
    st.markdown("## Epidemiological Intelligence & Spread Mapping")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        claim = st.text_area("Enter a health claim to analyze:", height=100, placeholder="e.g., 'Drinking hot water kills COVID instantly.'")
    with col2:
        analyze_btn = st.button("Analyze", use_container_width=True, key="analyze")
        spread_btn = st.button("Track Spread", use_container_width=True, key="spread")
    
    if analyze_btn and claim:
        with st.spinner("Analyzing claim..."):
            detection = TrackerCore.detect_misinformation(claim)
            severity_color = "🔴" if detection["severity"] == "High" else "🟠" if detection["severity"] == "Medium" else "🟢"
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Severity", detection["severity"], delta=severity_color)
            with col2:
                st.metric("Confidence", f"{detection['confidence']*100:.0f}%")
            with col3:
                st.metric("Keywords Found", len(detection['risk_keywords']))
            
            st.markdown("---")
            st.write(f"**Analyzed Claim:** {detection['text']}")
            if detection['risk_keywords']:
                st.write(f"**Risk Keywords:** {', '.join(detection['risk_keywords'])}")
            
            if detection["severity"] == "High":
                st.error("⚠️ CRITICAL: This contains dangerous health misinformation. Immediate intervention needed.")
            elif detection["severity"] == "Medium":
                st.warning("⚠️ WARNING: Misleading health claims detected. Recommend rapid fact-checking.")
            else:
                st.info("ℹ️ INFO: Post warrants monitoring. No immediate action required.")
    
    if spread_btn and claim:
        with st.spinner("Mapping spread network..."):
            network = TrackerCore.map_spread_network(claim)
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rumor ID", network['rumor_id'])
            with col2:
                st.metric("Total Reach", f"{network['total_reach']:,}")
            with col3:
                st.metric("Super-Spreaders", len(network['super_spreaders']))
            
            st.markdown("### Platform Spread")
            spread_cols = st.columns(len(network['spread_data']))
            for idx, (platform, data) in enumerate(network['spread_data'].items()):
                with spread_cols[idx]:
                    st.metric(platform, str(data).replace('{', '').replace('}', '')[:30])
            
            st.markdown("### Top Super-Spreaders")
            for spreader in network['super_spreaders'][:5]:
                with st.expander(f"👤 {spreader['account']} - {spreader['platform']}"):
                    st.write(f"**Followers:** {spreader['followers']:,}")
                    st.write(f"**Amplification Factor:** {spreader['amplification_factor']}x")

# ========================
# COMMUNITY SENTINEL PAGE
# ========================

elif page == "Community Sentinel":
    st.markdown("---")
    st.markdown("## Public Intervention & Localized Responses")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        claim = st.text_area("Enter misinformation to counter:", height=100, placeholder="e.g., 'Vaccines cause infertility'")
    with col2:
        intervene_btn = st.button("Generate Intervention", use_container_width=True, key="intervene")
        batch_btn = st.button("Batch Demo", use_container_width=True, key="batch")
    
    if intervene_btn and claim:
        with st.spinner("Generating intervention..."):
            detection = TrackerCore.detect_misinformation(claim)
            intervention = CommunitySentinel.generate_intervention(claim, detection["severity"])
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Post ID", intervention['post_id'])
            with col2:
                st.metric("Priority", intervention['priority_level'])
            with col3:
                st.metric("Type", intervention['intervention_type'])
            
            st.markdown("### Generated Response")
            st.success(intervention['response'])
            
            st.markdown("### Credible Sources")
            for source in intervention['credible_sources']:
                st.write(f"• {source}")
    
    if batch_btn:
        with st.spinner("Generating batch interventions..."):
            sample_claims = [m["text"] for m in misinformation_samples]
            interventions = CommunitySentinel.prioritize_interventions(sample_claims)
            
            st.markdown("---")
            critical = sum(1 for i in interventions if i["priority_level"] == "CRITICAL")
            high = sum(1 for i in interventions if i["priority_level"] == "HIGH")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Interventions", len(interventions))
            with col2:
                st.metric("Critical Priority", critical)
            with col3:
                st.metric("High Priority", high)
            
            st.markdown("---")
            for intervention in interventions:
                priority_color = "🔴" if intervention["priority_level"] == "CRITICAL" else "🟠" if intervention["priority_level"] == "HIGH" else "🟢"
                with st.expander(f"{priority_color} {intervention['priority_level']} - {intervention['original_claim'][:60]}..."):
                    st.write(f"**Claim:** {intervention['original_claim']}")
                    st.success(intervention['response'])

# ========================
# INSTITUTIONAL SHIELD PAGE
# ========================

elif page == "Institutional Shield":
    st.markdown("---")
    st.markdown("## Healthcare Provider Defense")
    
    institution = st.selectbox(
        "Select Institution",
        list(institutional_data.keys()),
        key="institution_select"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        monitor_btn = st.button("Monitor Threats", use_container_width=True, key="monitor")
    with col2:
        respond_btn = st.button("Generate Counter-Statement", use_container_width=True, key="respond")
    
    if monitor_btn:
        with st.spinner(f"Monitoring threats to {institution}..."):
            threats = InstitutionalShield.monitor_threats(institution)
            
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Institution", institution)
            with col2:
                st.metric("Threats Detected", len(threats))
            
            if threats:
                st.markdown("---")
                st.markdown("### Detected Threats")
                for threat in threats:
                    severity_color = "🔴" if threat["severity"] == "High" else "🟠"
                    with st.expander(f"{severity_color} {threat['threat_type']} - {threat['threat_id']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Claim:** {threat['claim']}")
                            st.write(f"**Type:** {threat['threat_type']}")
                        with col2:
                            st.write(f"**Reach:** {threat['reach']:,}")
                            st.write(f"**Origin:** {threat['origin']}")
                        st.write(f"**Coordinated Accounts:** {len(threat['coordinated_accounts'])} bot networks")
            else:
                st.success("No threats currently detected")
    
    if respond_btn:
        with st.spinner("Generating counter-statement..."):
            threats = InstitutionalShield.monitor_threats(institution)
            if threats:
                threat = threats[0]
                counter = InstitutionalShield.generate_counter_statement(institution, threat)
                
                st.markdown("---")
                st.markdown("### Threat Overview")
                with st.container():
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Threat ID:** {threat['threat_id']}")
                        st.write(f"**Type:** {threat['threat_type']}")
                    with col2:
                        st.write(f"**Reach:** {threat['reach']:,}")
                        st.write(f"**Severity:** {threat['severity']}")
                
                st.markdown("### Counter-Statement")
                st.info(counter['evidence_based_response'])
                
                st.markdown("### Supporting Sources")
                for source in counter['sources']:
                    st.write(f"• {source}")
                
                st.markdown("### Suggested Deployment Channels")
                channel_cols = st.columns(len(counter['suggested_channels']))
                for idx, channel in enumerate(counter['suggested_channels']):
                    with channel_cols[idx]:
                        st.write(f"📢 {channel}")
            else:
                st.info("No threats found for this institution")