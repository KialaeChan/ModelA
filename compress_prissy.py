#!/usr/bin/env python3
import json

filepath = '/home/claude/ModelA/definitions/couture_construction.json'
data = json.load(open(filepath))

# Shortened versions of existing prissy atoms
compressed = {
    "dress.trim_bow_cascade_vertical": "6-8 small bows (2-3cm) vertical down center front bodice. Bow waterfall. Coordinating pastels. Fun fancy decoration.",
    
    "dress.trim_pearl_button_parade": "12-20 tiny pearl buttons (4-6mm) down center front. Non-functional decoration. Tight row. Pearl white or pale pink.",
    
    "dress.trim_ribbon_corset_lacing": "Satin ribbon (5-8mm) criss-cross down back bodice. 6-8 crosses. Contrasting pastel. Bow at bottom. Fun lacing detail.",
    
    "dress.trim_horizontal_ruching_bands": "3-4 horizontal ruched bands (2-3cm) across bodice. Gathered texture. Contrasting or matching. Fun textured stripes.",
    
    "dress.collar_victorian_high_lace": "High standing lace collar (4-6cm) encircling neck. Stiffened. Elaborate lace pattern. Fun special day aesthetic.",
    
    "dress.detail_sleeve_bow_trim": "4-6 tiny bows (1-2cm) around puff sleeve edge. Bow ring. Contrasting pastel. Super fun sleeve detail.",
    
    "dress.detail_tier_seam_bow_parade": "8-12 small bows (2-3cm) at each tier seam. Encircling dress. Coordinating pastels. Fun decorative band.",
    
    "dress.detail_pompom_neckline_trim": "12-16 tiny pompoms (8-12mm) around neckline. Fluffy border. Coordinating pastels. Maximum cuteness.",
    
    "dress.trim_lace_bow_combo": "Gathered lace trim (2-3cm) with small bow (2cm) at center front. White lace, contrasting bow. Fun focal point.",
    
    "dress.trim_satin_rosette_cluster": "3-5 tiny rosettes (1-2cm) clustered at shoulder/waist/hip. Coordinating pastels. Dimensional flower grouping.",
    
    "dress.trim_rickrack_double_layer": "Two rickrack layers (5-8mm each) on hem/tiers. Contrasting pastels. Zigzag rainbow effect. Fun vintage detail.",
    
    "dress.trim_gathered_ribbon_swag": "Gathered satin ribbon (1-2cm) in swag pattern. Multiple swags. Contrasting pastel. Tiny bow at each point.",
    
    "dress.detail_waist_bow_bouquet": "5-7 small bows (2-3cm) clustered at waist side. Different pastels. Overlapping. Fun dimensional cluster.",
    
    "dress.detail_shoulder_bow_caps": "Large bows (6-8cm) on shoulder seams. Stand up from shoulders. Contrasting pastels. Fun shoulder accent.",
    
    "dress.trim_lace_insertion_vertical": "3-4 narrow lace strips (1-2cm) vertical in bodice front. White or cream. Fun striped effect. Special detail.",
    
    "dress.trim_pompom_hem_fringe": "20-30 pompoms (1-2cm) hanging from hem on threads. Multiple pastels. Bouncy fluffy border. Super fun.",
    
    "dress.detail_back_bow_trail": "Oversized bow (10-15cm) at back waist with long ribbons (30-40cm). Contrasting pastel. Dramatic back focal point.",
}

# Apply compressions
for key, new_content in compressed.items():
    if key in data:
        data[key]['contents'] = new_content

# Write back
with open(filepath, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

print(f"Compressed {len(compressed)} prissy atoms")
print("Ready to add TONS MORE!")
