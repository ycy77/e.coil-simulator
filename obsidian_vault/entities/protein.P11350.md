---
entity_id: "protein.P11350"
entity_type: "protein"
name: "narI"
source_database: "UniProt"
source_id: "P11350"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narI chlI b1227 JW1218"
---

# narI

`protein.P11350`

## Static

- Type: `protein`
- Source: `UniProt:P11350`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit. The γ subunit (NarI) of nitrate reductase A is a membrane-embedded heme-iron subunit resembling cytochrome b, which transfers electrons from the quinone pool to the β subunit (NarH). There are two hemes present, a low-potential heme bL and a high-potential heme bH . Electrons are thought to transfer from the quinol binding site (Q-site) via heme bL and heme bH to the [3Fe-4S] cluster of NarH . The Q-site of Nar is periplasmically oriented . NarI contains 5 transmembrane helices; the first helix appears to facilitate dimer formation. A C-terminal tail interacts with both NarG and NarH. The two Fe atoms are coordinated by histidine groups - His 56 and His 205 coordinate heme bH, His66 and His 187 coordinate heme bL. NarI contains an elongated hydrophobic cavity which may provide a protected interaction site for quinones . Reviews:

## Biological Role

Component of nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1227|gene.b1227]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11350`
- `KEGG:ecj:JW1218;eco:b1227;ecoc:C3026_07215;`
- `GeneID:945808;`
- `GO:GO:0005886; GO:0008940; GO:0009055; GO:0009061; GO:0009325; GO:0016020; GO:0019645; GO:0020037; GO:0042126; GO:0042128; GO:0044799; GO:0046872; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 1 gamma chain (EC 1.7.5.1) (Cytochrome B-NR) (Nitrate reductase A subunit gamma) (Quinol-nitrate oxidoreductase subunit gamma)
