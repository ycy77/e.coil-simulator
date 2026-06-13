---
entity_id: "protein.P0A7E1"
entity_type: "protein"
name: "pyrD"
source_database: "UniProt"
source_id: "P0A7E1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrD b0945 JW0928"
---

# pyrD

`protein.P0A7E1`

## Static

- Type: `protein`
- Source: `UniProt:P0A7E1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the conversion of dihydroorotate to orotate with quinone as electron acceptor. {ECO:0000269|PubMed:10074342}. Dihydroorotate dehydrogenase (PyrD) catalyzes the oxidation of dihydroorotate to orotate in the pathway for de novo biosynthesis of pyrimidine nucleotides. PyrD is a member of the membrane-associated family 2 dihydroorotate dehydrogenases and is linked with the electron transport system of the cell. When purified away from the membrane, the enzyme can be assayed as a dehydrogenase, using various quinones as well as ferricyanide or 2,6-dichlorophenolindolphenol (DCIP) as electron acceptors . There is evidence that the physiological electron acceptor is ubiquinone under aerobic conditions and menaquinone under anaerobic conditions . The enzyme works by a two-site ping-pong mechanism . The catalytically competent intermediate is the reduced enzyme - orotate complex . A reaction model for the first half reaction, flavin reduction, has been proposed . The available evidence is consistent with a stepwise mechanism of flavin reduction . The role of conserved residues near the active site has been investigated by site-directed mutagenesis . A crystal structure of PyrD has been solved at 2.5 Å resolution...

## Biological Role

Catalyzes DIHYDROOROTATE-DEHYDROGENASE-RXN (reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN), dihydroorotate dehydrogenase (reaction.ecocyc.RXN0-6491), RXN0-6554 (reaction.ecocyc.RXN0-6554). Bound by FMN (molecule.C00061).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of dihydroorotate to orotate with quinone as electron acceptor. {ECO:0000269|PubMed:10074342}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN|reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6491|reaction.ecocyc.RXN0-6491]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6554|reaction.ecocyc.RXN0-6554]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0945|gene.b0945]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7E1`
- `KEGG:ecj:JW0928;eco:b0945;ecoc:C3026_05790;`
- `GeneID:93776469;945556;`
- `GO:GO:0004152; GO:0005829; GO:0005886; GO:0006207; GO:0009220; GO:0010181; GO:0016020; GO:0044205; GO:0106430`
- `EC:1.3.5.2`

## Notes

Dihydroorotate dehydrogenase (quinone) (EC 1.3.5.2) (DHOdehase) (DHOD) (DHODase) (Dihydroorotate oxidase)
