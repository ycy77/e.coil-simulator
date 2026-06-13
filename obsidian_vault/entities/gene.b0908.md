---
entity_id: "gene.b0908"
entity_type: "gene"
name: "aroA"
source_database: "NCBI RefSeq"
source_id: "gene-b0908"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0908"
  - "aroA"
---

# aroA

`gene.b0908`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0908`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroA (gene.b0908) is a gene entity. It encodes aroA (protein.P0A6D3). Encoded protein function: FUNCTION: Catalyzes the transfer of the enolpyruvyl moiety of phosphoenolpyruvate (PEP) to the 5-hydroxyl of shikimate-3-phosphate (S3P) to produce enolpyruvyl shikimate-3-phosphate and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00210, ECO:0000269|PubMed:12430021, ECO:0000269|PubMed:13129913, ECO:0000269|PubMed:16225867, ECO:0000269|PubMed:17855366, ECO:0000269|PubMed:17958399, ECO:0000269|PubMed:19211556, ECO:0000269|PubMed:6229418}. EcoCyc product frame: AROA-MONOMER. Genomic coordinates: 958812-960095. EcoCyc protein note: 3-Phosphoshikimate-1-carboxyvinyltransferase (EPSP synthase) is involved in the 6th step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. EPSP synthase catalyzes the transfer of the enolpyruvoyl moiety from phosphoenolpyruvate to the hydroxyl group of carbon 5 of shikimate 3-phosphate with the elimination of phosphate to produce 5-enolpyruvoyl shikimate 3-phosphate (EPSP). This is an addition-elimination reaction. It is an ordered reaction in which shikimate 3-phosphate binds first. It involves the transfer of an enolpyruvyl group unchanged to the acceptor molecule...

## Biological Role

Repressed by lrp (protein.P0ACJ0), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6D3|protein.P0A6D3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=aroA; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=aroA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=aroA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003095,ECOCYC:EG10073,GeneID:945528`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:958812-960095:+; feature_type=gene
