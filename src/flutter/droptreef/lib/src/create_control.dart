import 'package:flet/flet.dart';

import 'droptreef.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "droptreef":
      return DroptreefControl(
        parent: args.parent!,
        control: args.control,
        children: args.children,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
