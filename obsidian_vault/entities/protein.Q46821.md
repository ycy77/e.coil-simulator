---
entity_id: "protein.Q46821"
entity_type: "protein"
name: "uacT"
source_database: "UniProt"
source_id: "Q46821"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22437829}; Multi-pass membrane protein {ECO:0000269|PubMed:22437829}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uacT ygfU b2888 JW5470"
---

# uacT

`protein.Q46821`

## Static

- Type: `protein`
- Source: `UniProt:Q46821`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22437829}; Multi-pass membrane protein {ECO:0000269|PubMed:22437829}.

## Enriched Summary

FUNCTION: Proton-dependent high-capacity transporter for uric acid. Also shows a low capacity for transport of xanthine at 37 degrees Celsius but not at 25 degrees Celsius. {ECO:0000269|PubMed:22437829}. UacT is low affinity, high capacity urate transporter in E.coli K-12. Over-expression of uacT from a plasmid results in uptake of labelled urate to high levels. Uptake is abolished by the addition of the protonophore, carbonyl cyanide m-chlorophenyl hydrazaone . UacT also transports xanthine but with low affinity and low capacity . UacT contains 10 transmembrane helices plus 4 smaller helical segments within the membrane; the amino and carboxy termini are located in the cytoplasm . Amino acid residues critical for function have been identified; threonine at position 100 is essential for uric acid specificity . The physiological significance of urate uptake is uncertain since no enzyme for the further catabolism of urate has been identified in E. coli . UacT is a member of the NCS2 family of nucleobase transporters. UacT: uric acid transporter

## Biological Role

Catalyzes xanthine:proton symport (reaction.ecocyc.RXN-5076), urate:proton symport (reaction.ecocyc.TRANS-RXN0-530). Transports 9H-purine-2,6,8-triol (molecule.ecocyc.CPD-15332), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Proton-dependent high-capacity transporter for uric acid. Also shows a low capacity for transport of xanthine at 37 degrees Celsius but not at 25 degrees Celsius. {ECO:0000269|PubMed:22437829}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-530|reaction.ecocyc.TRANS-RXN0-530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-15332|molecule.ecocyc.CPD-15332]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2888|gene.b2888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46821`
- `KEGG:ecj:JW5470;eco:b2888;ecoc:C3026_15835;`
- `GeneID:75172987;75205276;949017;`
- `GO:GO:0005886; GO:0015143; GO:0015293; GO:0015747; GO:0042906; GO:0042907; GO:1902600`

## Notes

Uric acid transporter UacT
