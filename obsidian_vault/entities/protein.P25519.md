---
entity_id: "protein.P25519"
entity_type: "protein"
name: "hflX"
source_database: "UniProt"
source_id: "P25519"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00900, ECO:0000269|PubMed:19181811}. Note=May associate with membranes."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hflX b4173 JW4131"
---

# hflX

`protein.P25519`

## Static

- Type: `protein`
- Source: `UniProt:P25519`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00900, ECO:0000269|PubMed:19181811}. Note=May associate with membranes.

## Enriched Summary

FUNCTION: GTPase that associates with the 50S ribosomal subunit and may have a role during protein synthesis or ribosome biogenesis. In vitro, also exhibits ATPase activity. {ECO:0000255|HAMAP-Rule:MF_00900, ECO:0000269|PubMed:19109926, ECO:0000269|PubMed:19181811, ECO:0000269|PubMed:19824612}. HflX is a heat shock-induced ribosome-dependent GTPase that rescues stalled ribosomes by dissociating vacant and mRNA-associated ribosomes with deacylated tRNA in the peptidyl site . Structural data suggests that HflX disrupts the central bridges between the ribosomal subunits and thereby promotes their dissociation . The HflX protein is a GTPase that interacts with the 50S subunit of the ribosome in the presence of both GTP, GDP, ATP and ADP . The intrinsic GTPase activity of HflX is very slow and can be stimulated 1000-fold by interaction with the 50S subunit as well as 70S ribosomes and poly(U)-programmed 70S ribosomes . GTP hydrolysis is required for ribosome dissociation or the release of HflX from the 50S subunit . HflX binds both GTP and ATP . Both the N-terminal and the C-terminal domain can bind and hydrolyze GTP and ATP . Purine nucleotide binding was studied by equilibrium and pre-steady-state fluorescence techniques...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: GTPase that associates with the 50S ribosomal subunit and may have a role during protein synthesis or ribosome biogenesis. In vitro, also exhibits ATPase activity. {ECO:0000255|HAMAP-Rule:MF_00900, ECO:0000269|PubMed:19109926, ECO:0000269|PubMed:19181811, ECO:0000269|PubMed:19824612}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4173|gene.b4173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25519`
- `KEGG:ecj:JW4131;eco:b4173;ecoc:C3026_22550;`
- `GeneID:948688;`
- `GO:GO:0003924; GO:0005524; GO:0005525; GO:0005737; GO:0005829; GO:0009408; GO:0016887; GO:0019843; GO:0032790; GO:0043022; GO:0043023; GO:0046872; GO:0072344; GO:0097216`

## Notes

GTPase HflX (GTP-binding protein HflX)
