/****************************************************************************
** Meta object code from reading C++ file 'dataclass.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.4.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../StandAlone/dataclass.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'dataclass.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.4.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_DataClass_t {
    QByteArrayData data[8];
    char stringdata[70];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_DataClass_t, stringdata) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_DataClass_t qt_meta_stringdata_DataClass = {
    {
QT_MOC_LITERAL(0, 0, 9), // "DataClass"
QT_MOC_LITERAL(1, 10, 11), // "setUsername"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 4), // "user"
QT_MOC_LITERAL(4, 28, 11), // "setPassword"
QT_MOC_LITERAL(5, 40, 4), // "pass"
QT_MOC_LITERAL(6, 45, 11), // "shellOutput"
QT_MOC_LITERAL(7, 57, 12) // "engagePython"

    },
    "DataClass\0setUsername\0\0user\0setPassword\0"
    "pass\0shellOutput\0engagePython"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_DataClass[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   34,    2, 0x0a /* Public */,
       4,    1,   37,    2, 0x0a /* Public */,
       6,    0,   40,    2, 0x0a /* Public */,
       7,    0,   41,    2, 0x0a /* Public */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    5,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void DataClass::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        DataClass *_t = static_cast<DataClass *>(_o);
        switch (_id) {
        case 0: _t->setUsername((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 1: _t->setPassword((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 2: _t->shellOutput(); break;
        case 3: _t->engagePython(); break;
        default: ;
        }
    }
}

const QMetaObject DataClass::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_DataClass.data,
      qt_meta_data_DataClass,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *DataClass::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *DataClass::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_DataClass.stringdata))
        return static_cast<void*>(const_cast< DataClass*>(this));
    return QObject::qt_metacast(_clname);
}

int DataClass::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 4;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
