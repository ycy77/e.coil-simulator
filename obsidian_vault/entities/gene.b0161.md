---
entity_id: "gene.b0161"
entity_type: "gene"
name: "degP"
source_database: "NCBI RefSeq"
source_id: "gene-b0161"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0161"
  - "degP"
---

# degP

`gene.b0161`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0161`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

degP (gene.b0161) is a gene entity. It encodes degP (protein.P0C0V0). Encoded protein function: FUNCTION: DegP acts as a chaperone at low temperatures but switches to a peptidase (heat shock protein) at higher temperatures (PubMed:10319814). Degrades transiently denatured and unfolded or misfolded proteins which accumulate in the periplasm following heat shock or other stress conditions (PubMed:16303867). DegP is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for beta-branched side chain amino acids (PubMed:8830688). Only unfolded proteins devoid of disulfide bonds appear capable of being cleaved, thereby preventing non-specific proteolysis of folded proteins (PubMed:8830688). Its proteolytic activity is essential for the survival of cells at elevated temperatures (PubMed:7557477). It can degrade IciA, Ada, casein, globin and PapA. DegP shares specificity with DegQ (PubMed:8830688). DegP is also involved in the biogenesis of partially folded outer-membrane proteins (OMP). {ECO:0000269|PubMed:10319814, ECO:0000269|PubMed:12730160, ECO:0000269|PubMed:16303867, ECO:0000269|PubMed:18496527, ECO:0000269|PubMed:18505836, ECO:0000269|PubMed:2180903, ECO:0000269|PubMed:7557477, ECO:0000269|PubMed:8830688}. EcoCyc product frame: EG10463-MONOMER. EcoCyc synonyms: htrA, ptd. Genomic coordinates: 180884-182308.

## Biological Role

Activated by cpxR (protein.P0AE88), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0V0|protein.P0C0V0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=degP; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=degP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000551,ECOCYC:EG10463,GeneID:947139`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:180884-182308:+; feature_type=gene
