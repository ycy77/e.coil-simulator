---
entity_id: "gene.b2311"
entity_type: "gene"
name: "ubiX"
source_database: "NCBI RefSeq"
source_id: "gene-b2311"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2311"
  - "ubiX"
---

# ubiX

`gene.b2311`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2311`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiX (gene.b2311) is a gene entity. It encodes ubiX (protein.P0AG03). Encoded protein function: FUNCTION: Flavin prenyltransferase that catalyzes the synthesis of the prenylated FMN cofactor (prenyl-FMN) for 4-hydroxy-3-polyprenylbenzoic acid decarboxylase UbiD. The prenyltransferase is metal-independent and links a dimethylallyl moiety from dimethylallyl monophosphate (DMAP) to the flavin N5 and C6 atoms of FMN (By similarity). Acts in concert with UbiD to perform the decarboxylation of 4-hydroxy-3-octaprenyl-benzoate, a step in the biosynthesis of coenzyme Q (PubMed:16923914, PubMed:17889824). {ECO:0000255|HAMAP-Rule:MF_01984, ECO:0000269|PubMed:16923914, ECO:0000269|PubMed:17889824}. EcoCyc product frame: UBIX-MONOMER. EcoCyc synonyms: dedF. Genomic coordinates: 2428057-2428626. EcoCyc protein note: Evidence gathered for orthologous enzymes and genetic interactions indicate that UbiX is a flavin prenyltransferase that produces a novel cofactor for CPLX0-301 UbiD, CPD-18260 . ubiX was first thought to encode a second 3-octaprenyl-4-hydroxybenzoate decarboxylase in E. coli ; however, no biochemical evidence for the enzymatic function of UbiX was available at that time. The fungal genes pad1 and fdc1 are homologs of E. coli ubiX and ubiD, respectively. Coexpression of Fdc1 from both Saccharomyces cerevisiae and Aspergillus niger with either the respective Pad1 enzymes or E...

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG03|protein.P0AG03]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=ubiX; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=ubiX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007628,ECOCYC:EG11044,GeneID:949033`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2428057-2428626:-; feature_type=gene
