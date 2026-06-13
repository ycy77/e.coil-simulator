---
entity_id: "protein.P37659"
entity_type: "protein"
name: "bcsG"
source_database: "UniProt"
source_id: "P37659"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcsG yhjU b3538 JW3506"
---

# bcsG

`protein.P37659`

## Static

- Type: `protein`
- Source: `UniProt:P37659`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

Cellulose biosynthesis protein BcsG bcsE, bcsF and bcsG are part of the bacterial cellulose synthesis gene cluster; in other organisms these genes are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In the cellulose producing K-12 strain AR3110, BcsG is a membrane anchored, Zn2+-dependent phosphoethanolamine (pEtN) transferase which, as part of a multisubunit cellulose synthase complex, modifies cellulose with an additional pEtN group on every other glucosyl residue; BcsG interacts with EG12264-MONOMER "BcsF" and the cellulose synthase catalytic subunit EG12260-MONOMER "BcsA" (and see ). In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology. A ΔbcsEFG mutation introduced into this strain leads to significantly reduced cellulose biosynthesis . In the cellulose producing strain E...

## Biological Role

Catalyzes RXN-19630 (reaction.ecocyc.RXN-19630).

## Annotation

Cellulose biosynthesis protein BcsG

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19630|reaction.ecocyc.RXN-19630]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3538|gene.b3538]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37659`
- `KEGG:ecj:JW3506;eco:b3538;ecoc:C3026_19165;`
- `GeneID:948058;`
- `GO:GO:0005886; GO:0030244`

## Notes

Cellulose biosynthesis protein BcsG
