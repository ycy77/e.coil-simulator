---
entity_id: "protein.P33358"
entity_type: "protein"
name: "mlrA"
source_database: "UniProt"
source_id: "P33358"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlrA yehV b2127 JW2115"
---

# mlrA

`protein.P33358`

## Static

- Type: `protein`
- Source: `UniProt:P33358`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activates transcription of csgD, the master regulator of biofilm formation, by binding to its promoter region (PubMed:11489123, PubMed:20874755). Also controls the transcription of cadC and ibaG (PubMed:20874755). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA (PubMed:23708798). {ECO:0000269|PubMed:11489123, ECO:0000269|PubMed:20874755, ECO:0000269|PubMed:23708798}. MlrA is a regulator of curli production in an avian pathogenic Escherichia coli strain and in Salmonella enterica serovar Typhimurium . Shiga toxin-encoding prophages have been observed to integrate at the mlrA gene of enterohemorrhagic E. coli . MlrA is a member of the MerR family, containing the conserved N-terminal DNA-binding domain present in members of this family . On the other hand, its C-terminal domain, probably used by a yet-to-be-identified effector, showed no similarity to any of the hitherto-characterized MerR family members . MlrA binds an AAAGTTGTACA(12N)TGCACAATTTT palindromic sequence and probably induces DNA underwinding, as in the case of MerR...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Activates transcription of csgD, the master regulator of biofilm formation, by binding to its promoter region (PubMed:11489123, PubMed:20874755). Also controls the transcription of cadC and ibaG (PubMed:20874755). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA (PubMed:23708798). {ECO:0000269|PubMed:11489123, ECO:0000269|PubMed:20874755, ECO:0000269|PubMed:23708798}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (10)

- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=MlrA; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=MlrA; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=MlrA; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=MlrA; target=csgD; function=+
- `activates` --> [[gene.b3183|gene.b3183]] `RegulonDB` `S` - regulator=MlrA; target=obgE; function=+
- `activates` --> [[gene.b3184|gene.b3184]] `RegulonDB` `S` - regulator=MlrA; target=yhbE; function=+
- `activates` --> [[gene.b3185|gene.b3185]] `RegulonDB` `S` - regulator=MlrA; target=rpmA; function=+
- `activates` --> [[gene.b3186|gene.b3186]] `RegulonDB` `S` - regulator=MlrA; target=rplU; function=+
- `activates` --> [[gene.b3190|gene.b3190]] `RegulonDB` `S` - regulator=MlrA; target=ibaG; function=+
- `activates` --> [[gene.b4133|gene.b4133]] `RegulonDB` `S` - regulator=MlrA; target=cadC; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2127|gene.b2127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33358`
- `KEGG:ecj:JW2115;eco:b2127;ecoc:C3026_11925;`
- `GeneID:75206373;949029;`
- `GO:GO:0003677; GO:0003700; GO:0006355`

## Notes

HTH-type transcriptional regulator MlrA (MerR-like regulator A)
