---
entity_id: "protein.P0AEL8"
entity_type: "protein"
name: "fimZ"
source_database: "UniProt"
source_id: "P0AEL8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fimZ ybcA b0535 JW5073"
---

# fimZ

`protein.P0AEL8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEL8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Response regulator that has two active forms, I and II, which are involved in cell surface extension and regulation of pili biosynthesis (PubMed:36057789). The active form I is required for constant cell elongation, possibly by stimulating the ATP synthesis activity of F-type ATPases (PubMed:36057789). The active form II activates expression of the sfmACDHF operon, which is involved in fimbriae formation, by binding directly to the sfmA promoter (PubMed:36057789). {ECO:0000269|PubMed:36057789}. FimZ is a positive DNA-binding transcriptional regulator that belongs to the LuxR/UhpA family of transcriptional regulators. FimZ's role as a regulator of fimbrial gene expression has been studied in Salmonella enterica; see e.g. . FimZ regulates pili biosynthesis and cell surface extension . FimZ has two active forms; active form I includes essential amino acid residues K106 and D109 to bind F-type ATPase, which induces constant cell elongation. The active form II requires the amino acid residue D56, a putative phosphorylation site, to activate the transcription of its targets . The genome-wide transcriptional profile in presence or absence of FimZ was characterized by microarrays; genes involved in the SOS response, fimbria formation, and putrescine biosynthesis were found to be differentially expressed...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Response regulator that has two active forms, I and II, which are involved in cell surface extension and regulation of pili biosynthesis (PubMed:36057789). The active form I is required for constant cell elongation, possibly by stimulating the ATP synthesis activity of F-type ATPases (PubMed:36057789). The active form II activates expression of the sfmACDHF operon, which is involved in fimbriae formation, by binding directly to the sfmA promoter (PubMed:36057789). {ECO:0000269|PubMed:36057789}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `activates` --> [[gene.b1298|gene.b1298]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1300|gene.b1300]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1301|gene.b1301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b0535|gene.b0535]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEL8`
- `KEGG:ecj:JW5073;eco:b0535;ecoc:C3026_02625;`
- `GeneID:947079;`
- `GO:GO:0000160; GO:0003677; GO:0005737; GO:0006355`

## Notes

HTH-type transcriptional regulator FimZ (FimZ orphan response regulator) (Fimbriae Z protein)
