---
entity_id: "gene.b3622"
entity_type: "gene"
name: "waaL"
source_database: "NCBI RefSeq"
source_id: "gene-b3622"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3622"
  - "waaL"
---

# waaL

`gene.b3622`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3622`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaL (gene.b3622) is a gene entity. It encodes waaL (protein.P27243). Encoded protein function: FUNCTION: Transferase involved in the biosynthesis of the lipopolysaccharide (LPS) (PubMed:21983211). In vitro, catalyzes the transfer of a polymerized O-antigen molecule from its polyprenyl diphosphate membrane anchor to a terminal sugar of the lipid A-core oligosaccharide, finalizing the biosynthesis of the lipopolysaccharide (PubMed:21983211, PubMed:30047569). The enzyme is functional and can be used to give diverse hybrid O-antigens in vitro, but K12 strains do not produce the O-antigen in vivo due to mutations in the rfb gene cluster (Probable). K12 strains are phenotypically rough, their lipopolysaccharide having a complete core structure, but no O-antigen (Probable). In highly mucoid K12 strains, WaaL can ligate colanic acid (CA or M-antigen) repeats to a significant proportion of lipopolysaccharide (LPS) core acceptor molecules, forming the LPS glycoform M(LPS) (PubMed:17227761). The attachment point was identified as O-7 of the L-glycero-D-manno-heptose of the outer LPS core, the same position used for O-antigen ligation (PubMed:17227761). Cannot catalyze ATP hydrolysis in vitro (PubMed:21983211). {ECO:0000269|PubMed:17227761, ECO:0000269|PubMed:21983211, ECO:0000269|PubMed:30047569, ECO:0000305|PubMed:9157235}. EcoCyc product frame: EG11424-MONOMER. EcoCyc synonyms: rfaL...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27243|protein.P27243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaL; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=waaL; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=waaL; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011849,ECOCYC:EG11424,GeneID:948148`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3796948-3798207:+; feature_type=gene
