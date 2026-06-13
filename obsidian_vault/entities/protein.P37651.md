---
entity_id: "protein.P37651"
entity_type: "protein"
name: "bcsZ"
source_database: "UniProt"
source_id: "P37651"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Secreted."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcsZ bcsC yhjM b3531 JW3499"
---

# bcsZ

`protein.P37651`

## Static

- Type: `protein`
- Source: `UniProt:P37651`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Secreted.

## Enriched Summary

FUNCTION: Hydrolyzes carboxymethylcellulose. The bcsZ gene encodes an endo-1,4-D-glucanase which belongs to glycosyl hydrolase family 8 . BcsZ has a predicted signal sequence ; a computational prediction that BcsZ is a lipoprotein is thought to be a probable false positive . In cell fractionation assays, the enzymatic activity appeared to be primarily extracellular , although the publication reported no positive controls. Crystal structures of apo-BcsZ and that of a catalytically inactive mutant bound to the substrate cellopentaose have been solved . BcsZ is encoded in a predicted operon together with bcsA, bcsB, and bcsC. In other organisms, these genes are involved in cellulose biosynthesis, a characteristic of the rdar morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology . BcsZ: "bacterial cellulose synthesis" Related review:

## Biological Role

Catalyzes RXN-2043 (reaction.ecocyc.RXN-2043).

## Annotation

FUNCTION: Hydrolyzes carboxymethylcellulose.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-2043|reaction.ecocyc.RXN-2043]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3531|gene.b3531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37651`
- `KEGG:ecj:JW3499;eco:b3531;ecoc:C3026_19130;`
- `GeneID:948046;`
- `GO:GO:0005576; GO:0008810; GO:0030245`
- `EC:3.2.1.4`

## Notes

Endoglucanase (EC 3.2.1.4) (Carboxymethylcellulase) (CMCase) (Cellulase) (Endo-1,4-beta-glucanase)
