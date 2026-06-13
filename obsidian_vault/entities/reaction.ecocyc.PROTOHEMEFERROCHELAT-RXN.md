---
entity_id: "reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN"
entity_type: "reaction"
name: "PROTOHEMEFERROCHELAT-RXN"
source_database: "EcoCyc"
source_id: "PROTOHEMEFERROCHELAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PROTOHEME FERRO-LYASE"
  - "HEME SYNTHETASE"
---

# PROTOHEMEFERROCHELAT-RXN

`reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROTOHEMEFERROCHELAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This is the last reaction in protoheme biosynthesis. EcoCyc reaction equation: PROTOHEME + PROTON -> PROTOPORPHYRIN_IX + FE+2; direction=REVERSIBLE. This is the last reaction in protoheme biosynthesis.

## Biological Role

Catalyzed by heme-containing peroxidase/deferrochelatase (complex.ecocyc.CPLX0-7810), hemH (protein.P23871), yfeX (protein.P76536). Substrates: H+ (molecule.C00080), protoheme (molecule.ecocyc.PROTOHEME). Products: Protoporphyrin (molecule.C02191), Fe2+ (molecule.C14818).

## Enriched Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)
- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Annotation

This is the last reaction in protoheme biosynthesis.

## Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)
- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7810|complex.ecocyc.CPLX0-7810]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23871|protein.P23871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76536|protein.P76536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROTOHEMEFERROCHELAT-RXN`

## Notes

PROTOHEME + PROTON -> PROTOPORPHYRIN_IX + FE+2; direction=REVERSIBLE
