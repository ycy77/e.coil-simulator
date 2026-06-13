---
entity_id: "protein.P0AER8"
entity_type: "protein"
name: "gltS"
source_database: "UniProt"
source_id: "P0AER8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17269795, ECO:0000269|PubMed:17662058, ECO:0000269|PubMed:2537813}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:17269795, ECO:0000269|PubMed:17662058}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltS gltC b3653 JW3628"
---

# gltS

`protein.P0AER8`

## Static

- Type: `protein`
- Source: `UniProt:P0AER8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17269795, ECO:0000269|PubMed:17662058, ECO:0000269|PubMed:2537813}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:17269795, ECO:0000269|PubMed:17662058}.

## Enriched Summary

FUNCTION: Catalyzes the sodium-dependent, binding-protein-independent transport of glutamate. {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}. E. coli contains four transporters for the uptake of glutamate (GltIJKL, GltP, GltS, and GadC). GltS accounts for approximately 25% of the total wild-type transport velocity of glutamate in aerobic growth with succinate and 40 mM NaCl . The membrane topology of GltS has been studied using PhoA and LacZ fusions to identify transmembrane segments and cytoplasmic and periplasmic domains . It was also studied using cysteine accessibility experiments of single-cysteine mutants . Both studies predict 10 transmembrane segments for the protein but differ slightly in their positions. GltS is a sodium dependent glutamate transporter which is specific for D- and L-glutamate. E. coli K12 cannot grow on glutamate as a sole carbon and nitrogen source. Selection of mutants which can grow on glutamate (Glt+) are typically due to mutations which overexpress either the GltS or GltP glutamate transporters . Transduction of a gltS knockout mutation into a gltS overexpressing strain renders the cell Glt-, and this phenotype could be complemented by the cloned gltS gene . Whole cell transport experiments have shown that GltS is sodium dependent with a Km of approx 1.5 μM...

## Biological Role

Catalyzes glutamate:Na+ symport (reaction.ecocyc.TRANS-RXN-122). Transports L-Glutamate (molecule.C00025).

## Annotation

FUNCTION: Catalyzes the sodium-dependent, binding-protein-independent transport of glutamate. {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-122|reaction.ecocyc.TRANS-RXN-122]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3653|gene.b3653]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AER8`
- `KEGG:ecj:JW3628;eco:b3653;ecoc:C3026_19790;`
- `GeneID:93778368;948166;`
- `GO:GO:0005886; GO:0015293; GO:0015501; GO:0015813`

## Notes

Sodium/glutamate symporter (Glutamate permease)
