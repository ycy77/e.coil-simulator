---
entity_id: "gene.b3626"
entity_type: "gene"
name: "waaJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3626"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3626"
  - "waaJ"
---

# waaJ

`gene.b3626`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3626`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaJ (gene.b3626) is a gene entity. It encodes waaJ (protein.P27129). Encoded protein function: FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10234827). Catalyzes the addition of a glucose (glucose III) to the outer-core glucose II (PubMed:10234827). {ECO:0000269|PubMed:10234827}. EcoCyc product frame: EG11353-MONOMER. EcoCyc synonyms: rfaJ, waaR. Genomic coordinates: 3800983-3801999. EcoCyc protein note: WaaJ (also known as WaaR and formerly RfaJ) is a UDP-glucose:(glucosyl)LPS α-1,2-glucosyltransferase which adds the third glucose (GlcIII) to the second glucose (GlcII) in the outer core of E. coli K-12 LPS . waaJ in E. coli K-12 is also referred to in the literature by the synonym WaaR. Early studies characterized the waa (rfa) locus and identified waaJ in both E. coli and Salmonella typhimurium . Later work renamed waaJ to waaR in E. coli K-12 to differentiate its activity (formation of α-D-Glcp-(1→2)-α-D-Glcp in the LPS outer core) from that of WaaJ in S. typhimurium (formation of α-D-Glcp-(1→2)-α-D-Galp) (see ). waaJ is predicted to encode a soluble or peripheral membrane protein; WaaJ activity requires functional waaB; WaaJ function is essential for Mu phage sensitivity...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27129|protein.P27129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011858,ECOCYC:EG11353,GeneID:948142`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3800983-3801999:-; feature_type=gene
