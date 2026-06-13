---
entity_id: "gene.b2400"
entity_type: "gene"
name: "gltX"
source_database: "NCBI RefSeq"
source_id: "gene-b2400"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2400"
  - "gltX"
---

# gltX

`gene.b2400`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2400`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltX (gene.b2400) is a gene entity. It encodes gltX (protein.P04805). Encoded protein function: FUNCTION: Catalyzes the attachment of glutamate to tRNA(Glu) in a two-step reaction: glutamate is first activated by ATP to form Glu-AMP and then transferred to the acceptor end of tRNA(Glu). {ECO:0000269|PubMed:14764088, ECO:0000269|PubMed:6280993, ECO:0000269|PubMed:6986385, ECO:0000269|PubMed:7797500, ECO:0000269|PubMed:8218204}.; FUNCTION: Phosphorylation of GltX by HipA prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to multidrug resistance and persistence (PubMed:24095282, PubMed:24343429). Overexpression of GltX prevents HipA-induced growth arrest, persister formation and increases in (p)ppGpp levels (PubMed:24343429, PubMed:28430938). {ECO:0000269|PubMed:24095282, ECO:0000269|PubMed:24343429, ECO:0000269|PubMed:28430938}. EcoCyc product frame: GLURS-MONOMER. EcoCyc synonyms: gltM, gluRS. Genomic coordinates: 2519257-2520672. EcoCyc protein note: Glutamate-tRNA ligase (GluRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules...

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04805|protein.P04805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gltX; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=gltX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007911,ECOCYC:EG10407,GeneID:946906`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2519257-2520672:-; feature_type=gene
