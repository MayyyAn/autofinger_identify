import json
from pyecharts import options as opts
from pyecharts.charts import Tree

f = open('./treedata.json')
data = json.load(f)


def transform_json(data):
    key, value = list(data.items())[0]
    lst = []
    for child in value['children']:
        if isinstance(child, dict):
            lst.append(transform_json(child))
        else:
            lst.append({'name': child})
    return {'name': key, "children": lst}


transform_data = transform_json(data)





tree = (
    Tree(init_opts=opts.InitOpts(width="1800px", height="20000px"))
        .add("",[transform_data], orient="LR", initial_tree_depth=1, collapse_interval=-1, is_roam=True,symbol_size=[2,2])
        #     参数layout的"radial"是径向布局是指以根节点为圆心，每一层节点为环，而"orthogonal"是正常的水平和垂直布局
        #     参数symbol是标记类型形状，提供的类型有:'emptyCircle', 'circle', 'rect', 'roundRect','triangle', 'diamond', 'pin', 'arrow'
        #     参数orient是布局方向，水平从左到右为"LR"，水平从右往左为"RL"，垂直从上到下为"TB",垂直从下到上为"BT"
        .set_global_opts(title_opts=opts.TitleOpts(title="指纹树"),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical", )
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)

tree.render("./devicetree.html")


