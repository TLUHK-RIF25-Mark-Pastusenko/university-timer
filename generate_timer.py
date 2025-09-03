#!/usr/bin/env python3

from datetime import datetime
import os

# create folder
os.makedirs('generated', exist_ok=True)

# setup timer start date
start_date = datetime(2025, 8, 28)  # Year, Month, Day
now = datetime.now()
diff = now - start_date

# calculate time
seconds = diff.total_seconds()
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
years = days // 365.25

# remains after coma
remaining_days = days % 365.25
remaining_hours = hours % 24
remaining_minutes = minutes % 60
remaining_seconds = seconds % 60

# time format
years_str = f"{int(years)}"
days_str = f"{int(remaining_days)}"
hours_str = f"{int(remaining_hours):02d}"
minutes_str = f"{int(remaining_minutes):02d}"
seconds_str = f"{int(remaining_seconds):02d}"

# Сcreate SVG
svg_content = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="180" viewBox="0 0 400 180">
  <style>
    .background {{
      fill: #0d1117;
      stroke: #30363d;
      stroke-width: 2;
    }}
    .text {{
      font: bold 14px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      fill: #c9d1d9;
    }}
    .label {{
      font: 12px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      fill: #8b949e;
    }}
    .number {{
      font: bold 20px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      fill: #58a6ff;
    }}
    .title {{
      font: bold 16px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      fill: #f0f6fc;
    }}
  </style>
  
  <rect class="background" x="10" y="10" width="380" height="160" rx="10" />
  
  <text class="title" x="200" y="40" text-anchor="middle">University Journey</text>
  
  <text class="number" x="80" y="80" text-anchor="middle">{years_str}</text>
  <text class="label" x="80" y="100" text-anchor="middle">YEARS</text>
  
  <text class="number" x="160" y="80" text-anchor="middle">{days_str}</text>
  <text class="label" x="160" y="100" text-anchor="middle">DAYS</text>
  
  <text class="number" x="240" y="80" text-anchor="middle">{hours_str}</text>
  <text class="label" x="240" y="100" text-anchor="middle">HOURS</text>
  
  <text class="number" x="320" y="80" text-anchor="middle">{minutes_str}</text>
  <text class="label" x="320" y="100" text-anchor="middle">MINUTES</text>
  
  <text class="text" x="200" y="140" text-anchor="middle">Since {start_date.strftime("%d %b %Y")}</text>
</svg>
'''

# save SVG
with open('generated/university_timer.svg', 'w') as f:
    f.write(svg_content)
