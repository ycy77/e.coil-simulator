---
entity_id: "gene.b1531"
entity_type: "gene"
name: "marA"
source_database: "NCBI RefSeq"
source_id: "gene-b1531"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1531"
  - "marA"
---

# marA

`gene.b1531`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1531`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

marA (gene.b1531) is a gene entity. It encodes marA (protein.P0ACH5). Encoded protein function: FUNCTION: May be a transcriptional activator of genes involved in the multiple antibiotic resistance (Mar) phenotype. It can also activate genes such as sodA, zwf and micF. EcoCyc product frame: PD00365. EcoCyc synonyms: norB, inaR, cfxB, nfxC, soxQ. Genomic coordinates: 1619574-1619957. EcoCyc protein note: MarA, "multiple antibiotic resistance" , participates in controlling several genes involved in resistance to antibiotics , oxidative stress , organic solvents , heavy metals , xenobiotics compounds , lipopolysaccharide (LPS) biosynthesis , and cell wall remodelling . The antibiotic resistance associated with MarA appears to involve the acidification of the cytoplasm . MarA, SoxS, and Rob are paralogous transcriptional regulators that show 45% amino acid identity between them ; the crystal structures for Rob and MarA confirm this similarity between them. They activate a common set of genes, but the expression and activity of each one of these proteins are induced by different signals. Many genes are regulated by all three proteins; however, some genes are regulated only by one of them. The differential regulation of these genes might be caused by the degeneracy of their DNA-binding sites...

## Biological Role

Repressed by cra (protein.P0ACP1), acrR (protein.P0ACS9), marR (protein.P27245). Activated by fis (protein.P0A6R3), soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACH5|protein.P0ACH5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=marA; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=marA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=marA; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `C` - regulator=Rob; target=marA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=marA; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=marA; function=-
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `S` - regulator=AcrR; target=marA; function=-
- `represses` <-- [[protein.P27245|protein.P27245]] `RegulonDB` `C` - regulator=MarR; target=marA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005112,ECOCYC:EG11434,GeneID:947613`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1619574-1619957:+; feature_type=gene
