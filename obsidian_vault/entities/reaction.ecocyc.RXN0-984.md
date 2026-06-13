---
entity_id: "reaction.ecocyc.RXN0-984"
entity_type: "reaction"
name: "RXN0-984"
source_database: "EcoCyc"
source_id: "RXN0-984"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-984

`reaction.ecocyc.RXN0-984`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-984`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA . AlkB-mediated repair involves hydroxylation of methylation lession coupled to decarboxylation of α-ketoglutarate, an unusual repair mechanism that regenerates the intact, unmethylated base . EcoCyc reaction equation: N1-METHYLADENINE + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> ADENINE + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT. AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA . AlkB-mediated repair involves hydroxylation of methylation lession coupled to decarboxylation of α-ketoglutarate, an unusual repair mechanism that regenerates the intact, unmethylated base .

## Biological Role

Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), N1-methyladenine (molecule.ecocyc.N1-METHYLADENINE). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), Adenine (molecule.C00147).

## Annotation

AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA . AlkB-mediated repair involves hydroxylation of methylation lession coupled to decarboxylation of α-ketoglutarate, an unusual repair mechanism that regenerates the intact, unmethylated base .

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N1-METHYLADENINE|molecule.ecocyc.N1-METHYLADENINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-984`

## Notes

N1-METHYLADENINE + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> ADENINE + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
