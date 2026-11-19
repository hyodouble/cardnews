ObjC.import('AppKit');
function run(argv) {
  var pb = $.NSPasteboard.generalPasteboard;
  var d = pb.dataForType($.NSPasteboardTypePNG);
  if (d.isNil()) d = pb.dataForType($.NSPasteboardTypeTIFF);
  if (d.isNil()) throw new Error('clipboard has no image');
  if (!d.writeToFileAtomically(argv[0], true)) throw new Error('write failed');
  return 'saved';
}
