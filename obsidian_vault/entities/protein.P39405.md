---
entity_id: "protein.P39405"
entity_type: "protein"
name: "fhuF"
source_database: "UniProt"
source_id: "P39405"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9990318}. Cell inner membrane {ECO:0000269|PubMed:9990318}; Peripheral membrane protein {ECO:0000269|PubMed:9990318}. Note=Loosely associated with the cytoplasmic membrane. {ECO:0000269|PubMed:9990318}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuF yjjS b4367 JW4331"
---

# fhuF

`protein.P39405`

## Static

- Type: `protein`
- Source: `UniProt:P39405`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9990318}. Cell inner membrane {ECO:0000269|PubMed:9990318}; Peripheral membrane protein {ECO:0000269|PubMed:9990318}. Note=Loosely associated with the cytoplasmic membrane. {ECO:0000269|PubMed:9990318}.

## Enriched Summary

FUNCTION: Siderophore-iron reductase which is involved in iron removal from the hydroxamate-type siderophores coprogen, ferrichrome and ferrioxamine B after their transport into the cell (PubMed:14756576). Binds both the iron-loaded and the apo forms of ferrichrome (PubMed:33559753). {ECO:0000269|PubMed:14756576, ECO:0000269|PubMed:33559753}. FhuF is a ferric-siderophore reductase that is able to mobilize iron from ferrioxamine B, ferrichrome and coprogen . FhuF contains a 2Fe-2S iron sulfur cluster . Residues C244, C245, C256, and C259 are involved in coordination of the cluster and are required for protein function. The Cys-Cys-Xaa10-Cys-Xaa2-Cys motif is unusual among 2Fe-2S proteins . Purified FhuF can directly reduce ferrioxamine B-bound ferric ions in vitro. The reduced ferrous ion is not bound to the [2Fe-2S] cluster. The system that regenerates reduced FhuF is not known . His-tagged FhuF has been overproduced and purified and structurally characterized by small-angle X-ray scattering and paramagnetic NMR spectroscopy . The reduction potential of FhuF has been measured and was found to be pH-dependent . In a sufD mutant, the FhuF protein is unstable . An fhuF mutant exhibits a defect in the utilization of ferrioxamine B as an iron source . The removal of iron from ferric coprogen and ferrichrome is significantly decreased in E. coli fhuF mutants. In an E...

## Biological Role

Catalyzes RXN0-7426 (reaction.ecocyc.RXN0-7426). Bound by a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

FUNCTION: Siderophore-iron reductase which is involved in iron removal from the hydroxamate-type siderophores coprogen, ferrichrome and ferrioxamine B after their transport into the cell (PubMed:14756576). Binds both the iron-loaded and the apo forms of ferrichrome (PubMed:33559753). {ECO:0000269|PubMed:14756576, ECO:0000269|PubMed:33559753}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7426|reaction.ecocyc.RXN0-7426]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4367|gene.b4367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39405`
- `KEGG:ecj:JW4331;eco:b4367;ecoc:C3026_23590;`
- `GeneID:948891;`
- `GO:GO:0000293; GO:0005829; GO:0005886; GO:0016722; GO:0033214; GO:0033215; GO:0046872; GO:0051537`

## Notes

Ferric siderophore reductase (Ferric iron reductase protein FhuF)
