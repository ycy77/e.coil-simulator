---
entity_id: "gene.b4662"
entity_type: "gene"
name: "sgrT"
source_database: "NCBI RefSeq"
source_id: "gene-b4662"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4662"
  - "sgrT"
---

# sgrT

`gene.b4662`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4662`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgrT (gene.b4662) is a gene entity. It encodes sgrT (protein.C1P5Z7). Encoded protein function: FUNCTION: Acts to promote recovery from glucose-phosphate stress due to intracellular accumulation of glucose-6-phosphate caused by disruption of glycolytic flux or in the presence of (toxic) non-metabolizable glucose phosphate analogs. It may do so by inhibiting the transporter activity for glucose uptake (PtsG) as cells that overexpress this protein do not seem to import glucose although they have nearly wild-type levels of PtsG. {ECO:0000269|PubMed:18042713}. EcoCyc product frame: MONOMER0-2842. Genomic coordinates: 77388-77519. EcoCyc protein note: sgrT is a conserved open reading frame located within the 5' end of the small RNA gene sgrS; sgrT is translated under sugar-phosphate stress (simulated by exposure of cells to α-methyl glucoside) and plays a role in the glucose-phosphate stress response. Ectopic expression of SgrT inhibits glucose transport and can promote recovery from sugar-phosphate stress ; however, it is not capable of rescue when produced from its native ribosome-binding site . Production of SgrT in E. coli K-12 appears to be low compared to that in Salmonella Typhimurium; a putative hairpin structure formed in the translation initiation region of sgrT may be responsible for repressing translation...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), rpoS (protein.P13445), sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P5Z7|protein.C1P5Z7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sgrT; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sgrT; function=+
- `activates` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=sgrT; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=sgrT; function=-

## External IDs

- `Dbxref:ECOCYC:G0-10617,GeneID:7751624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:77388-77519:+; feature_type=gene
