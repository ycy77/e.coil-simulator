---
entity_id: "protein.P75949"
entity_type: "protein"
name: "nagZ"
source_database: "UniProt"
source_id: "P75949"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagZ ycfO b1107 JW1093"
---

# nagZ

`protein.P75949`

## Static

- Type: `protein`
- Source: `UniProt:P75949`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Plays a role in peptidoglycan recycling by cleaving the terminal beta-1,4-linked N-acetylglucosamine (GlcNAc) from peptide-linked peptidoglycan fragments, giving rise to free GlcNAc, anhydro-N-acetylmuramic acid and anhydro-N-acetylmuramic acid-linked peptides. Cleaves GlcNAc linked beta-1,4 to MurNAc tripeptides. β-N-acetylglucosaminidase (NagZ) is a cytoplasmic enzyme involved in murein recycling. NagZ is specific for hydrolysis of the β-1,4 glycosidic bond, generating monosaccharides from the disaccharides released during muropeptide recycling. The enzyme cleaves anhydromuropeptides and is also active with muropeptides . A mutant strain lacking more than 99% of NagZ activity shows no apparent growth defect . A nagZ insertion mutant contains much increased amounts of the GlcNAc-β-1,4-anhydro-MurNAc disaccharide . The nagZ mRNA was predicted to be a regulatory hub for post-transcriptional regulation by small RNAs. Overexpression of RyhB and FnrS represses translation . NagZ: "β-N-acetylglucosaminidase" Reviews:

## Biological Role

Catalyzes chitobiose N-acetylglucosaminohydrolase (reaction.R00022), R07809 (reaction.R07809), R07810 (reaction.R07810), RXN0-5226 (reaction.ecocyc.RXN0-5226).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

FUNCTION: Plays a role in peptidoglycan recycling by cleaving the terminal beta-1,4-linked N-acetylglucosamine (GlcNAc) from peptide-linked peptidoglycan fragments, giving rise to free GlcNAc, anhydro-N-acetylmuramic acid and anhydro-N-acetylmuramic acid-linked peptides. Cleaves GlcNAc linked beta-1,4 to MurNAc tripeptides.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00022|reaction.R00022]] `KEGG` `database` - via EC:3.2.1.52
- `catalyzes` --> [[reaction.R07809|reaction.R07809]] `KEGG` `database` - via EC:3.2.1.52
- `catalyzes` --> [[reaction.R07810|reaction.R07810]] `KEGG` `database` - via EC:3.2.1.52
- `catalyzes` --> [[reaction.ecocyc.RXN0-5226|reaction.ecocyc.RXN0-5226]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1107|gene.b1107]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75949`
- `KEGG:ecj:JW1093;eco:b1107;ecoc:C3026_06680;`
- `GeneID:945671;`
- `GO:GO:0004563; GO:0005829; GO:0005975; GO:0008360; GO:0009252; GO:0009254; GO:0016231; GO:0051301; GO:0071555`
- `EC:3.2.1.52`

## Notes

Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase) (N-acetyl-beta-glucosaminidase)
