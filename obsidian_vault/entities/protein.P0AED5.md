---
entity_id: "protein.P0AED5"
entity_type: "protein"
name: "uvrY"
source_database: "UniProt"
source_id: "P0AED5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uvrY yecB b1914 JW1899"
---

# uvrY

`protein.P0AED5`

## Static

- Type: `protein`
- Source: `UniProt:P0AED5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). UvrY activates the transcription of the untranslated csrB RNA and of barA, in an autoregulatory loop. Mediates the effects of CsrA on csrB RNA by BarA-dependent and BarA-independent mechanisms (PubMed:12193630). {ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}. UvrY, which belongs to the LuxR/UhpA family, is the transcriptional regulator of the EG11367 BarA/EG11140 UvrY two-component signal transduction system which plays a role in central carbon metabolism via its regulation of the small non-coding RNAs CSRC-RNA "CsrC and CSRB-RNA "CsrB". BarA senses and responds to the presence of the protonated form of short-chain carboxylic acids such as FORMATE "formic acid" and ACET "acetic acid", which accumulate at the late exponential phase of growth on acetogenic substrates such as glucose. Upon sensing of these products, BarA autophosphorylates, followed by transphosphorylation of UvrY at the conserved Asp54 residue . Phosphorylated UvrY activates transcription of the G0-8785 and G0-8874 noncoding regulatory RNAs . These RNAs bind to the RNA-binding protein CPLX0-7956 CsrA, preventing it from interacting with its mRNA targets...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). UvrY activates the transcription of the untranslated csrB RNA and of barA, in an autoregulatory loop. Mediates the effects of CsrA on csrB RNA by BarA-dependent and BarA-independent mechanisms (PubMed:12193630). {ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (6)

- `activates` --> [[gene.b1501|gene.b1501]] `RegulonDB` `S` - regulator=UvrY; target=ydeP; function=+
- `activates` --> [[gene.b2687|gene.b2687]] `RegulonDB` `S` - regulator=UvrY; target=luxS; function=+
- `activates` --> [[gene.b3666|gene.b3666]] `RegulonDB` `S` - regulator=UvrY; target=uhpT; function=+
- `activates` --> [[gene.b4408|gene.b4408]] `RegulonDB` `S` - regulator=UvrY; target=csrB; function=+
- `activates` --> [[gene.b4457|gene.b4457]] `RegulonDB` `S` - regulator=UvrY; target=csrC; function=+
- `activates` --> [[gene.b4829|gene.b4829]] `RegulonDB` `S` - regulator=UvrY; target=uhpU; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b1914|gene.b1914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AED5`
- `KEGG:ecj:JW1899;eco:b1914;ecoc:C3026_10860;`
- `GeneID:93776219;946424;`
- `GO:GO:0000156; GO:0000160; GO:0000976; GO:0003700; GO:0005737; GO:0006355`

## Notes

Response regulator UvrY
