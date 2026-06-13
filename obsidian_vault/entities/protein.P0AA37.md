---
entity_id: "protein.P0AA37"
entity_type: "protein"
name: "rluA"
source_database: "UniProt"
source_id: "P0AA37"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluA yabO b0058 JW0057"
---

# rluA

`protein.P0AA37`

## Static

- Type: `protein`
- Source: `UniProt:P0AA37`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-746 in 23S ribosomal RNA and from uracil-32 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:10383384, ECO:0000269|PubMed:7493321}. RluA is the pseudouridine synthase that catalyzes formation of pseudouridine at position 746 in 23S rRNA and at position 32 in tRNAPhe . In vitro, the enzyme acts on free 23S rRNA fragments (bases 1-847) and tRNAPhe . Synthetic anticodon stem-loop containing RNAs are substrates of the enzyme . RNA containing 5-fluorouridine forms a covalent complex with and inhibits RluA stoichiometrically . The chemical fate of the complex has been probed using kinetic and labelling studies . Pre-steady-state kinetic analysis showed that at low RluA concentrations, substrate binding is rate-limiting, while at higher enzyme concentrations, catalysis is the rate-limiting step . A crystal structure of RluA bound to substrate RNA has been solved at 2.05 Å resolution. The enzyme induces significant reorganization of the RNA stem-loop structure, which may contribute to sequence recognition. The side chain of the R62 residue plays a key role in RluA activity by enabling the flipping of the U32 base into the active site of the enzyme...

## Biological Role

Catalyzes RXN-11842 (reaction.ecocyc.RXN-11842), RXN-11843 (reaction.ecocyc.RXN-11843).

## Annotation

FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-746 in 23S ribosomal RNA and from uracil-32 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:10383384, ECO:0000269|PubMed:7493321}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11842|reaction.ecocyc.RXN-11842]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11843|reaction.ecocyc.RXN-11843]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0058|gene.b0058]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA37`
- `KEGG:ecj:JW0057;eco:b0058;ecoc:C3026_00295;`
- `GeneID:93777379;946262;`
- `GO:GO:0000455; GO:0001522; GO:0003723; GO:0006364; GO:0008033; GO:0009451; GO:0009982; GO:0031118; GO:0031119; GO:0106029; GO:0120159; GO:0160142; GO:0160151`
- `EC:5.4.99.28; 5.4.99.29`

## Notes

Dual-specificity RNA pseudouridine synthase RluA (EC 5.4.99.28) (EC 5.4.99.29) (23S rRNA pseudouridine(746) synthase) (Ribosomal large subunit pseudouridine synthase A) (rRNA pseudouridylate synthase A) (rRNA-uridine isomerase A) (tRNA pseudouridine(32) synthase)
