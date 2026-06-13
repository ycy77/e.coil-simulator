---
entity_id: "protein.P0AA25"
entity_type: "protein"
name: "trxA"
source_database: "UniProt"
source_id: "P0AA25"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trxA fipA tsnC b3781 JW5856"
---

# trxA

`protein.P0AA25`

## Static

- Type: `protein`
- Source: `UniProt:P0AA25`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyzes dithiol-disulfide exchange reactions. Represents the oxidized form of RED-THIOREDOXIN-MONOMER. Thioredoxins are small electron transfer proteins that contain a cysteine disulfide/dithiol active site with the amino acid sequence motif Cys-X-X-Cys (where X is any amino acid). They are members of the thioredoxin protein family. Members of this family/superfamily contain the thioredoxin fold, a characteristic and stable protein fold consisting of four β-sheets surrounded by three α-helices (reviewed in ). The proteins function in a wide variety of cellular processes. Thioredoxin is reduced by NADPH in a reaction catalyzed by thioredoxin reductase. The conversion between the oxidized and reduced forms results in a subtle change of conformation. The functional properties differ between the two forms of thioredoxin. The reduced form of thioredoxin is a protein disulfide reductase, and catalyzes dithiol-disulfide exchange reactions. Escherichia coli thioredoxin contains the active site amino acid sequence Trp-Cys-Gly-Pro-Cys. In and reviewed in . Escherichia coli has two thioredoxins: RED-THIOREDOXIN-MONOMER "thioredoxin 1", encoded by the EG11031 gene, and RED-THIOREDOXIN2-MONOMER "thioredoxin 2", encoded by the EG11887 gene...

## Biological Role

Catalyzes RXN-20161 (reaction.ecocyc.RXN-20161).

## Annotation

FUNCTION: Participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyzes dithiol-disulfide exchange reactions.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-20161|reaction.ecocyc.RXN-20161]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3781|gene.b3781]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA25`
- `KEGG:ecj:JW5856;eco:b3781;ecoc:C3026_20470;`
- `GeneID:86861886;93778163;948289;`
- `GO:GO:0005737; GO:0005829; GO:0015035; GO:0030337; GO:0045454`

## Notes

Thioredoxin 1 (Trx-1)
