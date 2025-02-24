import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_simple_treeview/flutter_simple_treeview.dart';
import 'dart:convert'; // 用于 JSON 解析

class DroptreefControl extends StatefulWidget {
  final Control parent;
  final Control control;
  final List<Control> children;

  const DroptreefControl({
    super.key,
    required this.parent,
    required this.control,
    required this.children,
  });

  @override
  _DroptreefControlState createState() => _DroptreefControlState();
}

class _DroptreefControlState extends State<DroptreefControl> {
  @override
  Widget build(BuildContext context) {
    try {
      // 从 Python 传递的控制属性获取 JSON 字符串
      String jsonData = widget.control.attrString("nodesdata", "[]")!;

      // 解析 JSON 字符串为 Dart 列表
      List<dynamic> treeData = jsonDecode(jsonData);

      // 递归构建树形节点，限制深度为3
      List<TreeNode> buildTree(List<dynamic> data, int depth) {
        // 如果深度超过3层，停止递归
        if (depth > 3) return [];

        return data.map<TreeNode>((node) {
          return TreeNode(
            content: GestureDetector(
              onTap: () {
                // 检查节点是否有 URL，如果有，则打印 URL
                if (node["url"] != null) {
                  print("URL: ${node['url']}");
                }
              },
              child: Text(node["value"]),
            ),
            children:
                buildTree(node["children"] ?? [], depth + 1), // 递归构建子节点，并增加深度
          );
        }).toList();
      }

      // 从 widget.children 获取传递的子控件（例如 mywidget）
      Widget? myWidget;
      var ctrls = widget.children.where((c) => c.isVisible);
      if (ctrls.isNotEmpty) {
        myWidget = createControl(
            widget.control, ctrls.first.id, widget.control.isDisabled);
      }

      // 使用 flutter_simple_treeview 来渲染树
      return constrainedControl(
        context,
        Column(
          children: [
            // 渲染树形控件
            TreeView(
              nodes: buildTree(treeData, 1), // 从第一层开始构建树
            ),
            // 渲染传递的 mywidget 控件
            if (myWidget != null) myWidget,
          ],
        ),
        widget.parent,
        widget.control,
      );
    } catch (e, stackTrace) {
      print("Error: $e");
      print("Stack Trace: $stackTrace");
      return Center(child: Text("An error occurred: $e"));
    }
  }
}
