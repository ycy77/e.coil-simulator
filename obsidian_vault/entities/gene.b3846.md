---
entity_id: "gene.b3846"
entity_type: "gene"
name: "fadB"
source_database: "NCBI RefSeq"
source_id: "gene-b3846"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3846"
  - "fadB"
---

# fadB

`gene.b3846`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3846`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadB (gene.b3846) is a gene entity. It encodes fadB (protein.P21177). Encoded protein function: FUNCTION: Involved in the aerobic and anaerobic degradation of long-chain fatty acids via beta-oxidation cycle. Catalyzes the formation of 3-oxoacyl-CoA from enoyl-CoA via L-3-hydroxyacyl-CoA. It can also use D-3-hydroxyacyl-CoA and cis-3-enoyl-CoA as substrate. {ECO:0000255|HAMAP-Rule:MF_01621, ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:1748662, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629, ECO:0000269|PubMed:8755745}. EcoCyc product frame: FADB-MONOMER. EcoCyc synonyms: oldB. Genomic coordinates: 4028782-4030971. EcoCyc protein note: FadB is a multifunctional enzyme that is involved in the degradation of fatty acids via the β-oxidation cycle. Four enzymatic activities are associated with FadB: enoyl-CoA hydratase, 3-hydroxyacyl-CoA epimerase, 3-hydroxyacyl-CoA dehydrogenase, and Δ3-cis- Δ2-trans-enoyl-CoA isomerase . The 3-hydroxyacyl-CoA epimerase (EC 5.1.2.3) reaction occurs by a dehydration/hydration mechanism . The enoyl-CoA hydratase (EC 4.2.1.17) and 3-hydroxyacyl-CoA epimerase reactions are catalyzed by the same active site within the N-terminal domain of FadB. A Gly116Phe mutation eliminates both activities . The protonated γ-carboxylate of Glu139 and deprotonated γ-carboxylate of Glu119 provide acid/base functional groups for dehydration...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21177|protein.P21177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fadB; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=fadB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012564,ECOCYC:EG10279,GeneID:948336`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4028782-4030971:-; feature_type=gene
