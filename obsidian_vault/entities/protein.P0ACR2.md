---
entity_id: "protein.P0ACR2"
entity_type: "protein"
name: "punR"
source_database: "UniProt"
source_id: "P0ACR2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "punR ydhB b1659 JW1651"
---

# punR

`protein.P0ACR2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACR2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transcriptional regulator that activates the expression of punC, which encodes a purine nucleoside transporter (PubMed:34413462). In the presence of adenine, it binds to a conserved 23-bp palindromic motif in the intergenic region between punR and punC (PubMed:34413462). {ECO:0000269|PubMed:34413462}. PunR, formerly named YdhB, regulates a gene involved in the purine transport process in the presence of adenosine . This protein belongs to the LysR family of HTH-type transcriptional regulators . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain . PunR appears to recognize and bind to a palindromic DNA binding motif of 23 bp . Genome-wide PunR-binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The punR gene is located in the genome in an inverted position from its target gene . This arrangement in the genome appears to be conserved in other proteobacteria . Upstream of the punR gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the punR gene is affected by norfloxacin and glucose-acetate shift . A punR knockout mutant reduces cellular growth under nitrogen-limiting conditions .

## Annotation

FUNCTION: Transcriptional regulator that activates the expression of punC, which encodes a purine nucleoside transporter (PubMed:34413462). In the presence of adenine, it binds to a conserved 23-bp palindromic motif in the intergenic region between punR and punC (PubMed:34413462). {ECO:0000269|PubMed:34413462}.

## Outgoing Edges (1)

- `activates` --> [[gene.b1660|gene.b1660]] `RegulonDB|EcoCyc` `C` - regulator=PunR; target=punC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1659|gene.b1659]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACR2`
- `KEGG:ecj:JW1651;eco:b1659;ecoc:C3026_09520;`
- `GeneID:93775814;945208;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0006355`

## Notes

HTH-type transcriptional regulator PunR
