---
entity_id: "gene.b2926"
entity_type: "gene"
name: "pgk"
source_database: "NCBI RefSeq"
source_id: "gene-b2926"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2926"
  - "pgk"
---

# pgk

`gene.b2926`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2926`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgk (gene.b2926) is a gene entity. It encodes pgk (protein.P0A799). Encoded protein function: Phosphoglycerate kinase (EC 2.7.2.3) EcoCyc product frame: PGK. Genomic coordinates: 3071459-3072622. EcoCyc protein note: Phosphoglycerate kinase encoded by gene pgk catalyzes the reversible phosphorylation of 3-phospho-D-glycerate to 1,3-bisphospho-D-glycerate during glycolysis and gluconeogenesis in E. coli. In the glycolytic reaction direction the enzyme catalyzes the transfer of a phosphoryl group from 1,3-bisphospho-D-glycerate to ADP, forming ATP and 3-phospho-D-glycerate. Pgk cDNAs from a variety of organisms have been isolated. Their protein products are all monomers of similar size, with similar tertiary structures . The amino acid sequence of the E. coli enzyme is highly homologous to that of eukaryotes . Part of gene pgk showed similarity to an ORF found in the enterobacterial fish pathogen Edwardsiella ictaluri . The gene order around pgk in the Enterobacteriaceae differs from that in most other bacteria and transcriptional regulation of the E. coli epd-pgk-fbaA region has been studied . In earlier work, phosphoglycerate kinase was purified to near homogeneity from cell extracts of E. coli K-12. When assayed in the reverse direction its activity was dependent upon the presence of ATP and 3-phospho-D-glycerate...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A799|protein.P0A799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pgk; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=pgk; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=pgk; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=pgk; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009605,ECOCYC:EG10703,GeneID:947414`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3071459-3072622:-; feature_type=gene
