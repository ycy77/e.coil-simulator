---
entity_id: "gene.b0116"
entity_type: "gene"
name: "lpd"
source_database: "NCBI RefSeq"
source_id: "gene-b0116"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0116"
  - "lpd"
---

# lpd

`gene.b0116`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0116`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpd (gene.b0116) is a gene entity. It encodes lpdA (protein.P0A9P0). Encoded protein function: FUNCTION: Lipoamide dehydrogenase is a component of the glycine cleavage system as well as of the alpha-ketoacid dehydrogenase complexes. EcoCyc product frame: E3-MONOMER. EcoCyc synonyms: dhl, lpdA. Genomic coordinates: 127912-129336.

## Biological Role

Repressed by fnr (protein.P0A9E5), arcA (protein.P0A9Q1), pdhR (protein.P0ACL9), cra (protein.P0ACP1), btsR (protein.P0AFT5). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9P0|protein.P0A9P0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lpd; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=lpd; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=lpd; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=lpd; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=lpd; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=lpd; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=lpd; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=lpd; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=lpd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000404,ECOCYC:EG10543,GeneID:944854`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:127912-129336:+; feature_type=gene
