---
entity_id: "gene.b0405"
entity_type: "gene"
name: "queA"
source_database: "NCBI RefSeq"
source_id: "gene-b0405"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0405"
  - "queA"
---

# queA

`gene.b0405`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0405`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queA (gene.b0405) is a gene entity. It encodes queA (protein.P0A7F9). Encoded protein function: FUNCTION: Transfers and isomerizes the ribose moiety from AdoMet to the 7-aminomethyl group of 7-deazaguanine (preQ1-tRNA) to give epoxyqueuosine (oQ-tRNA). EcoCyc product frame: EG10812-MONOMER. EcoCyc synonyms: tsaA. Genomic coordinates: 425011-426081. EcoCyc protein note: S-adenosylmethionine:tRNA ribosyltransferase-isomerase (QueA) catalyzes addition of the 2,3-epoxy-4,5-dihydroxycyclopentane ring of epoxyqueuosine (oQ) to preQ1. This is the penultimate step in the formation of the queuosine (Q) anticodon loop modification in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) . The enzyme transfers the ribosyl moiety of SAM to preQ1 and isomerizes it to the epoxycyclopentane residue of oQ . A chemical reaction mechanism has been proposed . Inhibition studies are consistent with a fully ordered sequential bi-ter kinetic mechanism in which preQ1-tRNA binds first followed by SAM, with product release in the order adenine, methionine, and oQ-tRNA . Recognition of the tRNA substrate is mediated via the anticodon loop region . A queA mutant accumulates preQ1-modified tRNAs . The growth rate of the queA mutant is approximately half of that of the wild-type parent strain . Review:

## Biological Role

Activated by fis (protein.P0A6R3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7F9|protein.P0A7F9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=queA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001411,ECOCYC:EG10812,GeneID:944905`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:425011-426081:+; feature_type=gene
