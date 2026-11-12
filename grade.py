import streamlit as st

st.set_page_config(
    page_title="Grade Calculator",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "dark_mode" not in st.session_state:
  st.session_state.dark_mode = False

if "has_calculated" not in st.session_state:
  st.session_state.has_calculated = False

col_header_left, col_header_right = st.columns([10, 2])
with col_header_right:
  dark_mode = st.toggle("Dark Mode", value=st.session_state.dark_mode)
  st.session_state.dark_mode = dark_mode

if dark_mode:
  bg_main = "#0b1120"
  bg_card = "#1e293b"
  border_card = "#334155"
  text_main = "#f8fafc"
  text_sub = "#94a3b8"
  input_bg = "#0f172a"
  input_border = "#475569"
  input_text = "#f8fafc"
  input_placeholder = "#64748b"
  badge_bg = "#2563eb"
  badge_text = "#ffffff"
  stat_bg = "#0f172a"
  row_live_color = "#60a5fa"
  target_amber_bg = "#451a03"
  target_amber_border = "#78350f"
  target_amber_text = "#fef08a"
  target_green_bg = "#064e3b"
  target_green_border = "#065f46"
  target_green_text = "#a7f3d0"
  target_red_bg = "#450a0a"
  target_red_border = "#7f1d1d"
  target_red_text = "#fecaca"
else:
  bg_main = "#f1f5f9"
  bg_card = "#ffffff"
  border_card = "#cbd5e1"
  text_main = "#0f172a"
  text_sub = "#475569"
  input_bg = "#ffffff"
  input_border = "#cbd5e1"
  input_text = "#0f172a"
  input_placeholder = "#94a3b8"
  badge_bg = "#1e3a8a"
  badge_text = "#ffffff"
  stat_bg = "#f8fafc"
  row_live_color = "#1e3a8a"
  target_amber_bg = "#fefce8"
  target_amber_border = "#fef08a"
  target_amber_text = "#713f12"
  target_green_bg = "#f0fdf4"
  target_green_border = "#bbf7d0"
  target_green_text = "#14532d"
  target_red_bg = "#fef2f2"
  target_red_border = "#fecaca"
  target_red_text = "#7f1d1d"

st.markdown(
    f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    
    .stApp {{
        background-color: {bg_main} !important;
        color: {text_main} !important;
    }}

    div[data-testid="stTextInput"] input, 
    div[data-testid="stNumberInput"] input {{
        color: {input_text} !important;
        -webkit-text-fill-color: {input_text} !important;
        background-color: {input_bg} !important;
        border: 1px solid {input_border} !important;
        border-radius: 4px !important;
        font-size: 0.85rem !important;
    }}

    div[data-testid="stTextInput"] input::placeholder, 
    div[data-testid="stNumberInput"] input::placeholder {{
        color: {input_placeholder} !important;
        -webkit-text-fill-color: {input_placeholder} !important;
    }}

    div[data-testid="stButton"] button {{
        color: {text_main} !important;
        background-color: {bg_card} !important;
        border: 1px solid {border_card} !important;
        border-radius: 4px !important;
    }}

    div[data-testid="stButton"] button[kind="primary"] {{
        color: #ffffff !important;
        background-color: #1e3a8a !important;
        border: 1px solid #1e3a8a !important;
        font-weight: 600 !important;
    }}

    div[data-testid="stRadio"] label, 
    div[data-testid="stRadio"] label span,
    div[data-testid="stToggle"] label,
    div[data-testid="stToggle"] label span {{
        color: {text_main} !important;
    }}

    .custom-card {{
        background: {bg_card};
        border: 1px solid {border_card};
        border-radius: 4px;
        margin-bottom: 1rem;
        overflow: hidden;
    }}

    .card-header-blue {{
        background-color: #1e3a8a;
        color: #ffffff;
        padding: 0.75rem 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }}

    .card-header-dark {{
        background-color: #334155;
        color: #ffffff;
        padding: 0.75rem 1rem;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }}

    .badge-container {{
        text-align: center;
        background: {stat_bg};
        border: 1px solid {border_card};
        border-radius: 4px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }}
    
    .cgs-badge {{
        display: inline-block;
        background: {badge_bg};
        color: {badge_text} !important;
        font-size: 2rem;
        font-weight: 700;
        padding: 0.4rem 1.25rem;
        border-radius: 4px;
    }}

    .badge-point {{
        font-size: 1.25rem;
        font-weight: 700;
        color: {text_main};
        margin-top: 0.5rem;
    }}

    .badge-desc {{
        font-size: 0.85rem;
        font-weight: 500;
        color: {text_sub};
    }}

    .target-box-amber {{
        background: {target_amber_bg};
        border: 1px solid {target_amber_border};
        border-left: 4px solid #ca8a04;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        color: {target_amber_text};
        margin-top: 1rem;
        font-size: 0.85rem;
    }}
    
    .target-box-green {{
        background: {target_green_bg};
        border: 1px solid {target_green_border};
        border-left: 4px solid #16a34a;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        color: {target_green_text};
        margin-top: 1rem;
        font-size: 0.85rem;
    }}

    .target-box-red {{
        background: {target_red_bg};
        border: 1px solid {target_red_border};
        border-left: 4px solid #dc2626;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        color: {target_red_text};
        margin-top: 1rem;
        font-size: 0.85rem;
    }}
</style>
""",
    unsafe_allow_html=True,
)

CGS_SCALE = [
    (90.0, 100.0, 22, "A1", "First Class (Excellent)"),
    (85.0, 89.99, 21, "A2", "First Class (Very High)"),
    (80.0, 84.99, 20, "A3", "First Class (High)"),
    (75.0, 79.99, 19, "A4", "First Class (Clear)"),
    (70.0, 74.99, 18, "A5", "First Class"),
    (67.0, 69.99, 17, "B1", "Upper Second Class (Very High)"),
    (64.0, 66.99, 16, "B2", "Upper Second Class (High)"),
    (60.0, 63.99, 15, "B3", "Upper Second Class (Clear)"),
    (57.0, 59.99, 14, "C1", "Lower Second Class (Very High)"),
    (54.0, 56.99, 13, "C2", "Lower Second Class (High)"),
    (50.0, 53.99, 12, "C3", "Lower Second Class (Clear)"),
    (47.0, 49.99, 11, "D1", "Third Class (Very High)"),
    (44.0, 46.99, 10, "D2", "Third Class (High)"),
    (40.0, 43.99, 9, "D3", "Third Class (Pass)"),
    (35.0, 39.99, 8, "E1", "Marginal Fail"),
    (30.0, 34.99, 7, "E2", "Marginal Fail"),
    (25.0, 29.99, 6, "E3", "Marginal Fail"),
    (20.0, 24.99, 5, "F1", "Fail"),
    (15.0, 19.99, 4, "F2", "Fail"),
    (10.0, 14.99, 3, "F3", "Fail"),
    (5.0, 9.99, 2, "G1", "Bad Fail"),
    (1.0, 4.99, 1, "G2", "Bad Fail"),
    (0.0, 0.99, 0, "G3", "Bad Fail"),
]

LETTER_TO_DATA = {item[3]: item for item in CGS_SCALE}


def get_cgs_from_percentage(pct):
  pct = max(0.0, min(100.0, pct))
  for min_p, max_p, point, band, desc in CGS_SCALE:
    if pct >= min_p:
      rng = (max_p - min_p) if (max_p - min_p) > 0 else 1.0
      frac = (pct - min_p) / rng
      cgs_point = min(22.0, point + (frac * 0.99))
      return round(cgs_point, 2), band, desc
  return 0.0, "G3", "Bad Fail"


def gp_to_cgs(gp):
  rounded = min(22, max(0, round(gp)))
  for _, _, point, band, desc in CGS_SCALE:
    if point == rounded:
      return band, desc
  return "G3", "Bad Fail"


def parse_score(raw_input, is_cgs_mode=True):
  text = str(raw_input).strip().upper()
  if not text:
    return None, None, None

  if "/" in text:
    try:
      p, t = text.split("/")
      den = float(t.strip())
      if den <= 0:
        return None, None, None
      pct = (float(p.strip()) / den) * 100.0
      gp, band, _ = get_cgs_from_percentage(pct)
      return pct, gp, band
    except Exception:
      return None, None, None

  if is_cgs_mode and text in LETTER_TO_DATA:
    row = LETTER_TO_DATA[text]
    midpoint_pct = (row[0] + row[1]) / 2.0
    return midpoint_pct, float(row[2]), row[3]

  if is_cgs_mode and "GP" in text:
    try:
      val = float(text.replace("GP", "").strip())
      if 0 <= val <= 22:
        closest = min(CGS_SCALE, key=lambda x: abs(x[2] - val))
        midpoint_pct = (closest[0] + closest[1]) / 2.0
        return midpoint_pct, val, closest[3]
    except Exception:
      return None, None, None

  clean_num = text.replace("%", "").strip()
  try:
    val = float(clean_num)
    if is_cgs_mode and val <= 22.0 and ("%" not in text) and val.is_integer():
      closest = min(CGS_SCALE, key=lambda x: abs(x[2] - val))
      midpoint_pct = (closest[0] + closest[1]) / 2.0
      return midpoint_pct, val, closest[3]

    gp, band, _ = get_cgs_from_percentage(val)
    return val, gp, band
  except ValueError:
    return None, None, None


if "rows" not in st.session_state:
  st.session_state.rows = [
      {"name": "Homework 1 / Test 1", "grade": "42/50", "weight": 25.0},
      {"name": "Project", "grade": "80", "weight": 25.0},
      {"name": "Final Exam", "grade": "", "weight": 50.0},
  ]

with col_header_left:
  st.markdown(
      f"""
    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
        <div style="background-color: #1e3a8a; color: white; padding: 0.5rem 0.75rem; border-radius: 4px; font-weight: 700; font-size: 1.25rem;">
            22
        </div>
        <div>
            <h1 style="font-size: 1.4rem; font-weight: 700; color: {text_main}; margin: 0; line-height: 1.2;">
                Grade Calculator
            </h1>
            <p style="font-size: 0.8rem; color: {text_sub}; margin: 0;">
                Scottish CGS 22-Point & 100-Point System
            </p>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

st.write("")

mode = st.radio(
    "Grading Mode",
    options=[
        "Scottish CGS Calculator (22-Point Scale: A1 - G3)",
        "Normal 100-Point Calculator (Strictly Numeric)",
    ],
    horizontal=True,
    label_visibility="collapsed",
)
is_cgs = "Scottish CGS" in mode

st.write("")

left_col, right_col = st.columns([7, 5], gap="large")

with left_col:
  st.markdown(
      """
    <div class="custom-card" style="margin-bottom: 0.5rem;">
        <div class="card-header-blue">
            <span>Assessment Marks and Weighting</span>
            <span style="font-size: 0.75rem; color: #cbd5e1;">Active</span>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.caption(
      "Enter assessment details below. Supports fractions (42/50), percentages"
      " (84%), "
      + ("or CGS codes (A2, B1)." if is_cgs else "or decimals (85.5).")
  )

  th1, th2, th3, th4, th5 = st.columns([3.2, 2.2, 1.8, 2.0, 0.8])
  th1.markdown(
      f"<span style='font-size: 0.75rem; font-weight: 600; color: {text_sub};'>ASSIGNMENT / EXAM</span>",
      unsafe_allow_html=True,
  )
  th2.markdown(
      f"<span style='font-size: 0.75rem; font-weight: 600; color: {text_sub};'>GRADE</span>",
      unsafe_allow_html=True,
  )
  th3.markdown(
      f"<span style='font-size: 0.75rem; font-weight: 600; color: {text_sub};'>WEIGHT (%)</span>",
      unsafe_allow_html=True,
  )
  th4.markdown(
      f"<span style='font-size: 0.75rem; font-weight: 600; color: {text_sub}; text-align: right; display: block;'>{'CGS (0-22)' if is_cgs else 'SCORE (%)'}</span>",
      unsafe_allow_html=True,
  )
  th5.write("")

  delete_indices = []
  parsed_assignments = []
  total_accounted_weight = 0.0
  total_weighted_pct = 0.0
  total_weighted_cgs = 0.0

  for idx, item in enumerate(st.session_state.rows):
    r1, r2, r3, r4, r5 = st.columns([3.2, 2.2, 1.8, 2.0, 0.8])

    with r1:
      item["name"] = st.text_input(
          f"Name_{idx}",
          value=item["name"],
          key=f"name_{idx}",
          placeholder="e.g. Test 1",
          label_visibility="collapsed",
      )
    with r2:
      item["grade"] = st.text_input(
          f"Grade_{idx}",
          value=item["grade"],
          key=f"grade_{idx}",
          placeholder="42/50, A2" if is_cgs else "42/50, 84",
          label_visibility="collapsed",
      )
    with r3:
      item["weight"] = st.number_input(
          f"Weight_{idx}",
          value=float(item["weight"]),
          min_value=0.0,
          max_value=100.0,
          step=5.0,
          key=f"weight_{idx}",
          label_visibility="collapsed",
      )

    pct, gp, band = parse_score(item["grade"], is_cgs_mode=is_cgs)
    weight = item["weight"]

    with r4:
      if pct is not None:
        if is_cgs:
          st.markdown(
              f"<div style='text-align: right; font-weight: 600; color: {row_live_color}; padding-top: 0.5rem;'>{band} ({gp:.1f})</div>",
              unsafe_allow_html=True,
          )
        else:
          st.markdown(
              f"<div style='text-align: right; font-weight: 600; color: {row_live_color}; padding-top: 0.5rem;'>{pct:.2f}%</div>",
              unsafe_allow_html=True,
          )

        if weight > 0:
          w_frac = weight / 100.0
          total_weighted_pct += pct * w_frac
          total_weighted_cgs += gp * w_frac
          total_accounted_weight += weight
          parsed_assignments.append({
              "name": item["name"],
              "pct": pct,
              "gp": gp,
              "band": band,
              "weight": weight,
          })
      else:
        st.markdown(
            f"<div style='text-align: right; font-weight: 500; color: {input_placeholder}; padding-top: 0.5rem;'>--</div>",
            unsafe_allow_html=True,
        )

    with r5:
      if st.button("X", key=f"del_{idx}", help="Delete row"):
        delete_indices.append(idx)

  if delete_indices:
    for idx in sorted(delete_indices, reverse=True):
      st.session_state.rows.pop(idx)
    st.rerun()

  b_add, b_reset = st.columns([3, 7])
  with b_add:
    if st.button("Add Row", use_container_width=True):
      st.session_state.rows.append({"name": "", "grade": "", "weight": 0.0})
      st.rerun()
  with b_reset:
    if st.button("Reset Table", type="secondary"):
      st.session_state.rows = [
          {"name": "Assessment 1", "grade": "", "weight": 50.0},
          {"name": "Assessment 2", "grade": "", "weight": 50.0},
      ]
      st.session_state.has_calculated = False
      st.rerun()

  st.markdown(
      f"""
    <div style="background-color: {stat_bg}; border: 1px solid {border_card}; border-radius: 4px; padding: 0.75rem 1rem; margin-top: 1.5rem;">
        <span style="font-size: 0.75rem; font-weight: 600; color: {text_main}; text-transform: uppercase; letter-spacing: 0.05em;">
            Final Grade Planning (Optional)
        </span>
    </div>
    """,
      unsafe_allow_html=True,
  )

  t_col1, t_col2 = st.columns(2)
  with t_col1:
    target_goal = st.text_input(
        "Target Grade Goal",
        placeholder="e.g. A1, A2, B1 or 80" if is_cgs else "e.g. 75, 80",
    )
  with t_col2:
    suggested_remaining = max(0.0, 100.0 - total_accounted_weight)
    remaining_weight_input = st.number_input(
        "Remaining Weight (%)",
        value=float(suggested_remaining),
        min_value=0.0,
        max_value=100.0,
        step=5.0,
    )

  st.write("")
  if st.button("Calculate Grade", type="primary", use_container_width=True):
    st.session_state.has_calculated = True

with right_col:
  st.markdown(
      """
    <div class="custom-card" style="margin-bottom: 0;">
        <div class="card-header-dark">
            <span>Module Grade Summary</span>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  if st.session_state.has_calculated and total_accounted_weight > 0:
    if is_cgs:
      cgs_standing_point = total_weighted_cgs / (total_accounted_weight / 100.0)
      summary_band, summary_desc = gp_to_cgs(cgs_standing_point)
      badge_letter = summary_band
      badge_sub = f"{cgs_standing_point:.2f} / 22"
      badge_desc_text = summary_desc
    else:
      standing_pct = total_weighted_pct / (total_accounted_weight / 100.0)
      badge_letter = f"{standing_pct:.1f}%"
      badge_sub = f"{standing_pct:.2f} / 100.00"
      badge_desc_text = "Standard Percentage Standing"
    display_weighted_score = f"{total_weighted_pct:.2f}%"
    display_accounted_weight = f"{total_accounted_weight:.1f}%"
  else:
    badge_letter = "--"
    badge_sub = "-- / 22" if is_cgs else "-- / 100"
    badge_desc_text = (
        "Click 'Calculate Grade' to generate results"
        if not st.session_state.has_calculated
        else "Enter assessment marks to calculate"
    )
    display_weighted_score = "0.00%"
    display_accounted_weight = f"{total_accounted_weight:.1f}%"

  st.markdown(
      f"""
    <div class="custom-card" style="border-top: none; border-top-left-radius: 0; border-top-right-radius: 0;">
        <div class="card-body">
            <div class="badge-container">
                <div style="font-size: 0.75rem; font-weight: 600; color: {text_sub}; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
                    {'Overall CGS Grade' if is_cgs else 'Overall Percentage'}
                </div>
                <div class="cgs-badge">{badge_letter}</div>
                <div class="badge-point">{badge_sub}</div>
                <div class="badge-desc">{badge_desc_text}</div>
            </div>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  s1, s2 = st.columns(2)
  with s1:
    st.markdown(
        f"""
        <div style="background: {bg_card}; border: 1px solid {border_card}; border-radius: 4px; padding: 0.75rem; text-align: center;">
            <div style="font-size: 0.7rem; font-weight: 600; color: {text_sub}; text-transform: uppercase;">Weighted Score</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: {text_main};">{display_weighted_score}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with s2:
    st.markdown(
        f"""
        <div style="background: {bg_card}; border: 1px solid {border_card}; border-radius: 4px; padding: 0.75rem; text-align: center;">
            <div style="font-size: 0.7rem; font-weight: 600; color: {text_sub}; text-transform: uppercase;">Accounted Weight</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: {text_main};">{display_accounted_weight}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  if (
      st.session_state.has_calculated
      and target_goal.strip()
      and remaining_weight_input > 0
  ):
    target_pct, target_gp, target_band = parse_score(
        target_goal, is_cgs_mode=is_cgs
    )
    if target_pct is not None:
      needed_weighted = target_pct - total_weighted_pct
      needed_score_on_remaining = (
          needed_weighted / remaining_weight_input
      ) * 100.0

      if needed_score_on_remaining > 100.0:
        st.markdown(
            f"""
                <div class="target-box-red">
                    <strong>Target Unreachable:</strong> To reach <strong>{target_band if is_cgs else f"{target_pct:.1f}%"}</strong>, 
                    you would need <strong>{needed_score_on_remaining:.1f}%</strong> on the remaining {remaining_weight_input:.1f}% weight.
                </div>
                """,
            unsafe_allow_html=True,
        )
      elif needed_score_on_remaining <= 0.0:
        st.markdown(
            f"""
                <div class="target-box-green">
                    <strong>Target Guaranteed:</strong> You have already accumulated enough marks to guarantee a 
                    <strong>{target_band if is_cgs else f"{target_pct:.1f}%"}</strong> final grade.
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        req_gp, req_band, _ = get_cgs_from_percentage(needed_score_on_remaining)
        detail_txt = (
            f" (Grade <strong>{req_band} / {req_gp:.1f} pts</strong>)"
            if is_cgs
            else ""
        )
        st.markdown(
            f"""
                <div class="target-box-amber">
                    <strong>Target Required:</strong> To achieve a final grade of <strong>{target_band if is_cgs else f"{target_pct:.1f}%"}</strong>, 
                    you need at least <strong>{needed_score_on_remaining:.1f}%</strong>{detail_txt} across the remaining {remaining_weight_input:.1f}% of assessments.
                </div>
                """,
            unsafe_allow_html=True,
        )

  st.write("")

  if is_cgs:
    with st.expander("Scottish CGS 22-Point Mapping Scale", expanded=False):
      st.markdown(
          f"""
            <table style="width: 100%; font-size: 0.75rem; text-align: left; border-collapse: collapse;">
                <thead>
                    <tr style="border-bottom: 1px solid {border_card}; color: {text_sub};">
                        <th style="padding: 4px 6px;">Band</th>
                        <th style="padding: 4px 6px;">CGS Point</th>
                        <th style="padding: 4px 6px;">Percentage</th>
                        <th style="padding: 4px 6px;">Classification</th>
                    </tr>
                </thead>
                <tbody>
            """,
          unsafe_allow_html=True,
      )

      rows_html = ""
      for min_p, max_p, point, band, desc in CGS_SCALE:
        rows_html += f"""
                <tr style="border-bottom: 1px solid {border_card};">
                    <td style="padding: 4px 6px; font-weight: 600; color: {text_main};">{band}</td>
                    <td style="padding: 4px 6px; color: {text_sub};">{point}</td>
                    <td style="padding: 4px 6px; color: {text_sub};">{min_p:.0f}% - {max_p:.0f}%</td>
                    <td style="padding: 4px 6px; color: {text_sub}; font-size: 0.7rem;">{desc}</td>
                </tr>
                """

      st.markdown(rows_html + "</tbody></table>", unsafe_allow_html=True)
