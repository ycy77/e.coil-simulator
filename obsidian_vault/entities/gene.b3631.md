---
entity_id: "gene.b3631"
entity_type: "gene"
name: "waaG"
source_database: "NCBI RefSeq"
source_id: "gene-b3631"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3631"
  - "waaG"
---

# waaG

`gene.b3631`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3631`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaG (gene.b3631) is a gene entity. It encodes waaG (protein.P25740). Encoded protein function: FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10986272, PubMed:24479701). Catalyzes the addition of the first outer-core glucose from UDP-glucose to the inner-core heptose II (PubMed:24479701). Cannot use other sugar donors, such as UDP-galactose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can slowly hydrolyze UDP-glucose (PubMed:24479701). {ECO:0000269|PubMed:10986272, ECO:0000269|PubMed:24479701}. EcoCyc product frame: EG11339-MONOMER. EcoCyc synonyms: rfaG. Genomic coordinates: 3805943-3807067. EcoCyc protein note: The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . UDP-glucose:(heptosyl)lipopolysaccharide α-1,3-glucosyltransferase (WaaG) adds the first glucose (GlcI) of the outer core of LPS from UDP-glucose to the HepII residue of the inner core . WaaG is a glycosyltransferase family 4 (GT4) enzyme. Early studies characterized the rfa locus and identified the waaG gene (formerly rfaG) . waaG+ restores flagella and pili to a waaGPSBI deletion mutant...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25740|protein.P25740]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaG; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=waaG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011868,ECOCYC:EG11339,GeneID:948149`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3805943-3807067:-; feature_type=gene
