---
entity_id: "reaction.ecocyc.RXN0-2621"
entity_type: "reaction"
name: "RXN0-2621"
source_database: "EcoCyc"
source_id: "RXN0-2621"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2621

`reaction.ecocyc.RXN0-2621`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2621`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleotide excision repair (NER) is a generalized DNA repair process which can repair a wide diversity of DNA lesions including UV-induced photoproducts (cyclobutane dimers, 6-4 photoproducts, thymine glycol), bulky adducts, apurininc/apyrimidinic (AP) sites and cross-links. While some of these are also repaired by other pathways, in most cases NER is the major pathway for their repair. The nucleotide excision repair pathway consists of the following steps: recognition of the damaged area; incision 3' and 5' to the damaged area; excision of the damage-containing oligonucleotide; resynthesis of the excised strand and ligation to form a repaired duplex. The main constituents of the pathway are the products of the genes uvrA, uvrB and uvrC . EcoCyc reaction equation: CPD-8180 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. Nucleotide excision repair (NER) is a generalized DNA repair process which can repair a wide diversity of DNA lesions including UV-induced photoproducts (cyclobutane dimers, 6-4 photoproducts, thymine glycol), bulky adducts, apurininc/apyrimidinic (AP) sites and cross-links. While some of these are also repaired by other pathways, in most cases NER is the major pathway for their repair...

## Biological Role

Catalyzed by excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

Nucleotide excision repair (NER) is a generalized DNA repair process which can repair a wide diversity of DNA lesions including UV-induced photoproducts (cyclobutane dimers, 6-4 photoproducts, thymine glycol), bulky adducts, apurininc/apyrimidinic (AP) sites and cross-links. While some of these are also repaired by other pathways, in most cases NER is the major pathway for their repair. The nucleotide excision repair pathway consists of the following steps: recognition of the damaged area; incision 3' and 5' to the damaged area; excision of the damage-containing oligonucleotide; resynthesis of the excised strand and ligation to form a repaired duplex. The main constituents of the pathway are the products of the genes uvrA, uvrB and uvrC .

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2621`

## Notes

CPD-8180 + ATP + WATER -> a-post-excision-UvrCB-DNA-complex + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
