---
entity_id: "protein.P28634"
entity_type: "protein"
name: "trmO"
source_database: "UniProt"
source_id: "P28634"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmO tsaA yaeB b0195 JW0191"
---

# trmO

`protein.P28634`

## Static

- Type: `protein`
- Source: `UniProt:P28634`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: S-adenosyl-L-methionine-dependent methyltransferase responsible for the addition of the methyl group in the formation of N6-methyl-N6-threonylcarbamoyladenosine at position 37 (m(6)t(6)A37) of the tRNA anticodon loop of tRNA(Thr)(GGU) that read codons starting with adenosine (PubMed:25063302, PubMed:9537379). The methyl group of m(6)t(6)A37 appears to slightly improve the efficiency of the tRNA decoding ability (PubMed:25063302, PubMed:9537379). {ECO:0000269|PubMed:25063302, ECO:0000269|PubMed:9537379}. tRNA m6t6A37 methyltransferase (TrmO) catalyzes methylation of N6 of the A37 nucleotide adjacent to the anticodon of tRNAs thrT-tRNA and thrV-tRNA. The presence of the N6-threonylcarbamoyl modification at A37 is required for activity of the enzyme . TrmO is able to discriminate between the four Thr-specific tRNAs in E. coli, only modifying the ACY-specific tRNAs containing the GGU anticodon. The major specificity determinants within these tRNAs are C31-G39 and G34 . TrmO is the founding member of a novel class of SAM-dependent methyltransferases. Site-directed mutagenesis of conserved residues that were expected to be involved in SAM binding confirmed that Arg92 and Lys136 are critical for TrmO activity . tRNA in a strain carrying the tsaA1 allele, which maps to 4.6 min on the E. coli chromosome, lacks m6t6A...

## Biological Role

Catalyzes RXN0-7114 (reaction.ecocyc.RXN0-7114).

## Annotation

FUNCTION: S-adenosyl-L-methionine-dependent methyltransferase responsible for the addition of the methyl group in the formation of N6-methyl-N6-threonylcarbamoyladenosine at position 37 (m(6)t(6)A37) of the tRNA anticodon loop of tRNA(Thr)(GGU) that read codons starting with adenosine (PubMed:25063302, PubMed:9537379). The methyl group of m(6)t(6)A37 appears to slightly improve the efficiency of the tRNA decoding ability (PubMed:25063302, PubMed:9537379). {ECO:0000269|PubMed:25063302, ECO:0000269|PubMed:9537379}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7114|reaction.ecocyc.RXN0-7114]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0195|gene.b0195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28634`
- `KEGG:ecj:JW0191;eco:b0195;ecoc:C3026_00905;`
- `GeneID:93777228;949112;`
- `GO:GO:0000049; GO:0030488; GO:0089715`
- `EC:2.1.1.-`

## Notes

tRNA (adenine(37)-N6)-methyltransferase (EC 2.1.1.-) (tRNA (m6t6A37) methyltransferase) (tRNA methyltransferase O)
