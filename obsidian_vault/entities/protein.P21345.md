---
entity_id: "protein.P21345"
entity_type: "protein"
name: "gltP"
source_database: "UniProt"
source_id: "P21345"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1971622, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:28025687}; Multi-pass membrane protein {ECO:0000250|UniProtKB:O59010}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltP b4077 JW4038"
---

# gltP

`protein.P21345`

## Static

- Type: `protein`
- Source: `UniProt:P21345`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:1971622, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:28025687}; Multi-pass membrane protein {ECO:0000250|UniProtKB:O59010}.

## Enriched Summary

FUNCTION: Catalyzes the proton-dependent, binding-protein-independent transport of glutamate and aspartate (PubMed:1971622, PubMed:2537813, PubMed:28025687, PubMed:336628, PubMed:8596452). At least two protons are transported in symport with the substrate (PubMed:8596452). Binds glutamate and aspartate, and it has an approximately four-fold higher affinity for binding L-aspartate than L-glutamate in native membranes (PubMed:28025687). {ECO:0000269|PubMed:1971622, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:28025687, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}. E. coli contains four transporters for the uptake of glutamate (GltIJKL, GltP, GltS, and GadC) and five transporters for the uptake of aspartate (GltIJKL, GltP, DctA, DcuA, and DcuB). GltP accounts for approximately 60% of the total wild-type transport velocity of glutamate, and 52% of the total wild-type transport velocity of aspartate in aerobic growth with succinate and 40 mM NaCl . GltP is a proton dependent transporter for glutamate and aspartate. E. coli K12 cannot grow on glutamate as a sole carbon and nitrogen source, selection of mutants which can grow on glutamate (Glt+) are typically due to mutations which overexpress either the GltS or GltP glutamate transporters . The cloned gltP gene has been shown to confer the ability to utilize and transport glutamate and aspartate...

## Biological Role

Catalyzes aspartate:proton symport (reaction.ecocyc.TRANS-RXN-122A), L-glutamate:proton symport (reaction.ecocyc.TRANS-RXN-162). Transports L-Glutamate (molecule.C00025).

## Annotation

FUNCTION: Catalyzes the proton-dependent, binding-protein-independent transport of glutamate and aspartate (PubMed:1971622, PubMed:2537813, PubMed:28025687, PubMed:336628, PubMed:8596452). At least two protons are transported in symport with the substrate (PubMed:8596452). Binds glutamate and aspartate, and it has an approximately four-fold higher affinity for binding L-aspartate than L-glutamate in native membranes (PubMed:28025687). {ECO:0000269|PubMed:1971622, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:28025687, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-122A|reaction.ecocyc.TRANS-RXN-122A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-162|reaction.ecocyc.TRANS-RXN-162]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4077|gene.b4077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21345`
- `KEGG:ecj:JW4038;eco:b4077;ecoc:C3026_22035;`
- `GeneID:948591;`
- `GO:GO:0005280; GO:0005886; GO:0006835; GO:0022857`

## Notes

Glutamate/aspartate-proton symporter GltP (Glutamate-aspartate carrier protein) (Proton-glutamate-aspartate transport protein)
