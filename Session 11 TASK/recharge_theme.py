import os
import seaborn as sns

def apply_corporate_theme():
    sns.set_theme(
        style='whitegrid',
        context='talk',
        palette='colorblind',
        font_scale=0.9,
        rc={'axes.spines.top': False, 'axes.spines.right': False}
    )

def export_chart(fig, name):
    folder = 'report_visuals'
    os.makedirs(folder, exist_ok=True)
    
    png_path = os.path.join(folder, f'{name}.png')
    svg_path = os.path.join(folder, f'{name}.svg')
    
    fig.savefig(png_path, dpi=300, bbox_inches='tight')
    fig.savefig(svg_path, bbox_inches='tight')
    return png_path, svg_path