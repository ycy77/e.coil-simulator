---
entity_id: "protein.C1P605"
entity_type: "protein"
name: "azuC"
source_database: "UniProt"
source_id: "C1P605"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}; Peripheral membrane protein {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "azuC b4663 JW1891.1"
---

# azuC

`protein.C1P605`

## Static

- Type: `protein`
- Source: `UniProt:C1P605`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}; Peripheral membrane protein {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}.

## Enriched Summary

Uncharacterized protein AzuC The AzuC coding sequence lies within an RNA initially called G0-17112 IsrB and later AzuCR . AzuCR is a dual-function RNA which can also act as the RNA0-430 AzuR regulatory small RNA. The AzuC coding sequence overlaps the AzuR base-pairing region; AzuC and AzuR activities compete, that is, the mRNA and base-pairing activities of the AzuCR RNA interfere with each other . AzuC interacts with AERGLYC3PDEHYDROG-MONOMER and increases dehydrogenase activity; the physiological relevance of this is uncertain but it may serve to modulate membrane composition . AzuC is predicted to form an amphipathic helix; the protein localizes to the inner membrane . AzuC levels (detected as the sequential peptide affinity (SPA)-tagged protein) are higher in cells grown with glucose compared to those grown with glycerol or galactose due to cAMP receptor protein (CRP)-mediated repression ; AzuC-SPA levels are also repressed under low-oxygen conditions, are moderately induced during heat shock, oxidative stress, and thiol stress, and are substantially increased under acidic (pH 5.5) conditions . A discordance between AzuC-SPA protein level (high) and AzuCR RNA level (low) is observed when cells are grown to stationary phase in glycerol at pH 5.5...

## Annotation

Uncharacterized protein AzuC

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b4663|gene.b4663]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:C1P605`
- `KEGG:eco:b4663;`
- `GeneID:7751642;86946758;93776206;`
- `GO:GO:0005886; GO:0008047`

## Notes

Uncharacterized protein AzuC
