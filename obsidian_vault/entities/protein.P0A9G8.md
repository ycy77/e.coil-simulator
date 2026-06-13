---
entity_id: "protein.P0A9G8"
entity_type: "protein"
name: "modE"
source_database: "UniProt"
source_id: "P0A9G8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:9210473}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "modE modR b0761 JW0744"
---

# modE

`protein.P0A9G8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9G8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:9210473}.

## Enriched Summary

FUNCTION: Functions as an intracellular molybdate sensor. The ModE-Mo complex acts as a repressor of the modABC operon, which is involved in the transport of molybdate (PubMed:8550508). Binds modA promoter DNA in the absence of molybdate, however molybdate binding confers increased DNA affinity (PubMed:9044285, PubMed:9210473). Binds the promoter of moaA activating its transcription; binding is not enhanced by molybdate (PubMed:9044285). The protein dimer binds the consensus palindrome sequence 5'-TATAT-N7-TAYAT-3' and a variant 5'-TGTGT-N7-TGYGT-3' (PubMed:16205910, PubMed:9044285, PubMed:9210473). Acts as a regulator of the expression of 67 genes, many of which encode molybdoenzymes, acts both directly and indirectly (PubMed:10206709, PubMed:16205910, PubMed:9466267). ModE also binds tungstate (PubMed:11259434, PubMed:9210473). {ECO:0000269|PubMed:10206709, ECO:0000269|PubMed:11259434, ECO:0000269|PubMed:16205910, ECO:0000269|PubMed:8550508, ECO:0000269|PubMed:9044285, ECO:0000269|PubMed:9210473, ECO:0000269|PubMed:9466267}.

## Biological Role

Component of DNA-binding transcriptional dual regulator ModE (complex.ecocyc.CPLX0-2541).

## Annotation

FUNCTION: Functions as an intracellular molybdate sensor. The ModE-Mo complex acts as a repressor of the modABC operon, which is involved in the transport of molybdate (PubMed:8550508). Binds modA promoter DNA in the absence of molybdate, however molybdate binding confers increased DNA affinity (PubMed:9044285, PubMed:9210473). Binds the promoter of moaA activating its transcription; binding is not enhanced by molybdate (PubMed:9044285). The protein dimer binds the consensus palindrome sequence 5'-TATAT-N7-TAYAT-3' and a variant 5'-TGTGT-N7-TGYGT-3' (PubMed:16205910, PubMed:9044285, PubMed:9210473). Acts as a regulator of the expression of 67 genes, many of which encode molybdoenzymes, acts both directly and indirectly (PubMed:10206709, PubMed:16205910, PubMed:9466267). ModE also binds tungstate (PubMed:11259434, PubMed:9210473). {ECO:0000269|PubMed:10206709, ECO:0000269|PubMed:11259434, ECO:0000269|PubMed:16205910, ECO:0000269|PubMed:8550508, ECO:0000269|PubMed:9044285, ECO:0000269|PubMed:9210473, ECO:0000269|PubMed:9466267}.

## Outgoing Edges (42)

- `activates` --> [[gene.b0781|gene.b0781]] `RegulonDB` `S` - regulator=ModE; target=moaA; function=+
- `activates` --> [[gene.b0782|gene.b0782]] `RegulonDB` `S` - regulator=ModE; target=moaB; function=+
- `activates` --> [[gene.b0783|gene.b0783]] `RegulonDB` `S` - regulator=ModE; target=moaC; function=+
- `activates` --> [[gene.b0784|gene.b0784]] `RegulonDB` `S` - regulator=ModE; target=moaD; function=+
- `activates` --> [[gene.b0785|gene.b0785]] `RegulonDB` `S` - regulator=ModE; target=moaE; function=+
- `activates` --> [[gene.b1221|gene.b1221]] `RegulonDB` `S` - regulator=ModE; target=narL; function=+
- `activates` --> [[gene.b1222|gene.b1222]] `RegulonDB` `S` - regulator=ModE; target=narX; function=+
- `activates` --> [[gene.b2194|gene.b2194]] `RegulonDB` `C` - regulator=ModE; target=ccmH; function=+
- `activates` --> [[gene.b2195|gene.b2195]] `RegulonDB` `C` - regulator=ModE; target=ccmG; function=+
- `activates` --> [[gene.b2196|gene.b2196]] `RegulonDB` `C` - regulator=ModE; target=ccmF; function=+
- `activates` --> [[gene.b2197|gene.b2197]] `RegulonDB` `C` - regulator=ModE; target=ccmE; function=+
- `activates` --> [[gene.b2198|gene.b2198]] `RegulonDB` `C` - regulator=ModE; target=ccmD; function=+
- `activates` --> [[gene.b2199|gene.b2199]] `RegulonDB` `C` - regulator=ModE; target=ccmC; function=+
- `activates` --> [[gene.b2200|gene.b2200]] `RegulonDB` `C` - regulator=ModE; target=ccmB; function=+
- `activates` --> [[gene.b2201|gene.b2201]] `RegulonDB` `C` - regulator=ModE; target=ccmA; function=+
- `activates` --> [[gene.b2202|gene.b2202]] `RegulonDB` `C` - regulator=ModE; target=napC; function=+
- `activates` --> [[gene.b2203|gene.b2203]] `RegulonDB` `C` - regulator=ModE; target=napB; function=+
- `activates` --> [[gene.b2204|gene.b2204]] `RegulonDB` `C` - regulator=ModE; target=napH; function=+
- `activates` --> [[gene.b2205|gene.b2205]] `RegulonDB` `C` - regulator=ModE; target=napG; function=+
- `activates` --> [[gene.b2206|gene.b2206]] `RegulonDB` `C` - regulator=ModE; target=napA; function=+
- `activates` --> [[gene.b2207|gene.b2207]] `RegulonDB` `C` - regulator=ModE; target=napD; function=+
- `activates` --> [[gene.b2208|gene.b2208]] `RegulonDB` `C` - regulator=ModE; target=napF; function=+
- `activates` --> [[gene.b2717|gene.b2717]] `RegulonDB` `S` - regulator=ModE; target=hycI; function=+
- `activates` --> [[gene.b2718|gene.b2718]] `RegulonDB` `S` - regulator=ModE; target=hycH; function=+
- `activates` --> [[gene.b2719|gene.b2719]] `RegulonDB` `S` - regulator=ModE; target=hycG; function=+
- `activates` --> [[gene.b2720|gene.b2720]] `RegulonDB` `S` - regulator=ModE; target=hycF; function=+
- `activates` --> [[gene.b2721|gene.b2721]] `RegulonDB` `S` - regulator=ModE; target=hycE; function=+
- `activates` --> [[gene.b2722|gene.b2722]] `RegulonDB` `S` - regulator=ModE; target=hycD; function=+
- `activates` --> [[gene.b2723|gene.b2723]] `RegulonDB` `S` - regulator=ModE; target=hycC; function=+
- `activates` --> [[gene.b2724|gene.b2724]] `RegulonDB` `S` - regulator=ModE; target=hycB; function=+
- `activates` --> [[gene.b2725|gene.b2725]] `RegulonDB` `S` - regulator=ModE; target=hycA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-2541|complex.ecocyc.CPLX0-2541]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0763|gene.b0763]] `RegulonDB` `C` - regulator=ModE; target=modA; function=-
- `represses` --> [[gene.b0764|gene.b0764]] `RegulonDB` `C` - regulator=ModE; target=modB; function=-
- `represses` --> [[gene.b0765|gene.b0765]] `RegulonDB` `C` - regulator=ModE; target=modC; function=-
- `represses` --> [[gene.b0894|gene.b0894]] `RegulonDB` `C` - regulator=ModE; target=dmsA; function=-
- `represses` --> [[gene.b0895|gene.b0895]] `RegulonDB` `C` - regulator=ModE; target=dmsB; function=-
- `represses` --> [[gene.b0896|gene.b0896]] `RegulonDB` `C` - regulator=ModE; target=dmsC; function=-
- `represses` --> [[gene.b4381|gene.b4381]] `RegulonDB` `S` - regulator=ModE; target=deoC; function=-
- `represses` --> [[gene.b4382|gene.b4382]] `RegulonDB` `S` - regulator=ModE; target=deoA; function=-
- `represses` --> [[gene.b4383|gene.b4383]] `RegulonDB` `S` - regulator=ModE; target=deoB; function=-
- `represses` --> [[gene.b4384|gene.b4384]] `RegulonDB` `S` - regulator=ModE; target=deoD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0761|gene.b0761]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9G8`
- `KEGG:ecj:JW0744;eco:b0761;ecoc:C3026_03860;`
- `GeneID:75170760;945366;`
- `GO:GO:0000987; GO:0005829; GO:0006355; GO:0015689; GO:0030151; GO:0045892; GO:0045893; GO:1990198; GO:2000143`

## Notes

DNA-binding transcriptional dual regulator ModE
