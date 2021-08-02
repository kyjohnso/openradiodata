import datetime
from app import db, orm

class Raw(db.Model):
    __tablename__ = 'raw'
    id = db.Column(db.Integer, primary_key=True)
    Manufacturer = db.Column(db.String(80))
    Model = db.Column(db.String(80))
    UploadDateTime = db.Column(
        db.DateTime,
        index=True, 
        default=datetime.datetime.utcnow
    )
    MeasurementDateTime = db.Column(db.DateTime, index=True)
    ElapsedRealtimeMillis = db.Column(db.Integer)
    TimeNanos = db.Column(db.BigInteger)
    LeapSecond = db.Column(db.Integer)
    TimeUncertaintyNanos = db.Column(db.Integer)
    FullBiasNanos = db.Column(db.BigInteger)
    BiasNanos = db.Column(db.Float)
    BiasUncertaintyNanos = db.Column(db.Float)
    DriftNanosPerSecond = db.Column(db.Float)
    DriftUncertaintyNanosPerSecond = db.Column(db.Float)
    HardwareClockDiscontinuityCount = db.Column(db.Float)
    Svid = db.Column(db.SmallInteger, index=True)
    TimeOffsetNanos = db.Column(db.Float)
    State = db.Column(db.Integer)
    ReceivedSvTimeNanos = db.Column(db.BigInteger, index=True)
    ReceivedSvTimeUncertaintyNanos = db.Column(db.Float)
    Cn0DbHz = db.Column(db.Float)
    PseudorangeRateMetersPerSecond = db.Column(db.Float)
    PseudorangeRateUncertaintyMetersPerSecond = db.Column(db.Float)
    AccumulatedDeltaRangeState = db.Column(db.Float)
    AccumulatedDeltaRangeMeters = db.Column(db.Float)
    AccumulatedDeltaRangeUncertaintyMeters = db.Column(db.Float)
    CarrierFrequencyHz = db.Column(db.Float)
    CarrierCycles = db.Column(db.Float)
    CarrierPhase = db.Column(db.Float)
    CarrierPhaseUncertainty = db.Column(db.Float)
    MultipathIndicator = db.Column(db.Float)
    SnrInDb = db.Column(db.Float)
    ConstellationType = db.Column(db.SmallInteger,index=True) 
    AgcDb = db.Column(db.Float)
    fix_id = db.Column(db.Integer, db.ForeignKey('fix.id'))

class Fix(db.Model):
    __tablename__ = 'fix'
    id = db.Column(db.Integer, primary_key=True)
    raws = orm.relationship("Raw")
    UploadDateTime = db.Column(
        db.DateTime,
        index=True, 
        default=datetime.datetime.utcnow
    )
    MeasurementDateTime = db.Column(db.DateTime, index=True)
    Provider = db.Column(db.String(80))
    Latitude = db.Column(db.Float,index=True)
    Longitude = db.Column(db.Float,index=True)
    Altitude = db.Column(db.Float)
    Speed = db.Column(db.Float)
    Accuracy = db.Column(db.Float)
    UTCTimeInMs = db.Column(db.BigInteger, index=True)

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    UploadDateTime = db.Column(
        db.DateTime,
        index=True, 
        default=datetime.datetime.utcnow
    )
    String = db.Column(db.String(80))
    Float = db.Column(db.Float)
    
