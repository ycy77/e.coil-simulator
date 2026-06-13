---
entity_id: "gene.b0639"
entity_type: "gene"
name: "nadD"
source_database: "NCBI RefSeq"
source_id: "gene-b0639"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0639"
  - "nadD"
---

# nadD

`gene.b0639`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0639`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadD (gene.b0639) is a gene entity. It encodes nadD (protein.P0A752). Encoded protein function: FUNCTION: Catalyzes the reversible adenylation of nicotinate mononucleotide (NaMN) to nicotinic acid adenine dinucleotide (NaAD). {ECO:0000269|PubMed:10894752}. EcoCyc product frame: NICONUCADENYLYLTRAN-MONOMER. EcoCyc synonyms: ybeN, fusB. Genomic coordinates: 669931-670572. EcoCyc protein note: Nicotinate-mononucleotide adenylyltransferase (NadD) is an essential enzyme involved in both de novo biosynthesis and salvage of NAD+ . Its essentiality makes it a target for the development of antibacterial agents . Both nicotinic acid mononucleotide (NaMN) and nicotinamide mononucleotide (NMN) are substrates, but the rate of adenylation of NaMN is at least 20 times faster than that of NMN . Crystal structures of the enzyme alone and in a complex with deamido-NAD have been solved and show that ligand binding causes conformational changes in regions surrounding the active site . nadD is essential for growth . The nadD72 mutant allele was first isolated as a spontaneous temperature-sensitive mutation that leads to higher tolerance to fusidic acid. The mutant phenotype is pleiotropic . Further characterization of this mutation showed it to be an allele of nadD with a -1 frameshift mutation that leads to a change in the C terminus of the NadD protein...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A752|protein.P0A752]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nadD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002187,ECOCYC:G6350,GeneID:945248`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:669931-670572:-; feature_type=gene
