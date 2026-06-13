---
entity_id: "reaction.ecocyc.RXN-15119"
entity_type: "reaction"
name: "RXN-15119"
source_database: "EcoCyc"
source_id: "RXN-15119"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15119

`reaction.ecocyc.RXN-15119`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15119`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Wild-type E. coli has a low level of resistance to tellurite resulting from its reduction to elemental tellurium by the membrane associated enzymes, nitrate reductase A and nitrate reductase Z. A very low level of tellurite reductase activity is also present in the cytoplasmic fraction of anaerobically grown E. coli cells . Reduction of tellurite results in superoxide (O2-) generation EcoCyc reaction equation: CPD-4544 + Donor-H2 -> CPD-16009 + Acceptor; direction=LEFT-TO-RIGHT. Wild-type E. coli has a low level of resistance to tellurite resulting from its reduction to elemental tellurium by the membrane associated enzymes, nitrate reductase A and nitrate reductase Z. A very low level of tellurite reductase activity is also present in the cytoplasmic fraction of anaerobically grown E. coli cells . Reduction of tellurite results in superoxide (O2-) generation

## Biological Role

Catalyzed by cupric reductase RclA (complex.ecocyc.CPLX0-8542), lipoamide dehydrogenase (complex.ecocyc.E3-CPLX), nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX), nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX). Substrates: tellurite (molecule.ecocyc.CPD-4544). Products: Te0 (molecule.ecocyc.CPD-16009).

## Annotation

Wild-type E. coli has a low level of resistance to tellurite resulting from its reduction to elemental tellurium by the membrane associated enzymes, nitrate reductase A and nitrate reductase Z. A very low level of tellurite reductase activity is also present in the cytoplasmic fraction of anaerobically grown E. coli cells . Reduction of tellurite results in superoxide (O2-) generation

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8542|complex.ecocyc.CPLX0-8542]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-16009|molecule.ecocyc.CPD-16009]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15119`

## Notes

CPD-4544 + Donor-H2 -> CPD-16009 + Acceptor; direction=LEFT-TO-RIGHT
