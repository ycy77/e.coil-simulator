---
entity_id: "protein.P06134"
entity_type: "protein"
name: "ada"
source_database: "UniProt"
source_id: "P06134"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ada b2213 JW2201"
---

# ada

`protein.P06134`

## Static

- Type: `protein`
- Source: `UniProt:P06134`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the adaptive response to alkylation damage in DNA caused by alkylating agents. Repairs O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme (Cys-321). Also specifically repairs the Sp diastereomer of DNA methylphosphotriester lesions by the same mechanism, although the methyl transfer occurs onto a different cysteine residue (Cys-38). Cannot demethylate the other diastereomer, Rp-methylphosphotriester. This is a suicide reaction: the enzyme is irreversibly inactivated. {ECO:0000269|PubMed:2987862}.; FUNCTION: The methylation of Ada by methylphosphotriesters in DNA leads to its activation as a transcriptional regulator that activates the transcription of its own gene, ada, and other alkylation resistance genes, alkA, alkB and aidB. {ECO:0000269|PubMed:2987862}. ada encodes a bifunctional methyltransferase and transcriptional regulator which is a key component of the adaptive response - the mechanism of adaption induced after exposure to small amounts of DNA alkylating agents. O6-methylguanine (O6--meG) and O4-methylthymine (O4-meT) are two of a number of nucleobase modifications that result from exposure of DNA to alkylating agents - both chemical [eg...

## Biological Role

Catalyzes 2.1.1.63-RXN (reaction.ecocyc.2.1.1.63-RXN), RXN-17823 (reaction.ecocyc.RXN-17823), RXN-17824 (reaction.ecocyc.RXN-17824).

## Annotation

FUNCTION: Involved in the adaptive response to alkylation damage in DNA caused by alkylating agents. Repairs O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme (Cys-321). Also specifically repairs the Sp diastereomer of DNA methylphosphotriester lesions by the same mechanism, although the methyl transfer occurs onto a different cysteine residue (Cys-38). Cannot demethylate the other diastereomer, Rp-methylphosphotriester. This is a suicide reaction: the enzyme is irreversibly inactivated. {ECO:0000269|PubMed:2987862}.; FUNCTION: The methylation of Ada by methylphosphotriesters in DNA leads to its activation as a transcriptional regulator that activates the transcription of its own gene, ada, and other alkylation resistance genes, alkA, alkB and aidB. {ECO:0000269|PubMed:2987862}.

## Outgoing Edges (9)

- `activates` --> [[gene.b2068|gene.b2068]] `RegulonDB` `C` - regulator=Ada; target=alkA; function=+
- `activates` --> [[gene.b2212|gene.b2212]] `RegulonDB` `C` - regulator=Ada; target=alkB; function=-+
- `activates` --> [[gene.b2213|gene.b2213]] `RegulonDB` `C` - regulator=Ada; target=ada; function=-+
- `activates` --> [[gene.b4187|gene.b4187]] `RegulonDB` `S` - regulator=Ada; target=aidB; function=+
- `catalyzes` --> [[reaction.ecocyc.2.1.1.63-RXN|reaction.ecocyc.2.1.1.63-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17823|reaction.ecocyc.RXN-17823]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17824|reaction.ecocyc.RXN-17824]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `represses` --> [[gene.b2212|gene.b2212]] `RegulonDB` `C` - regulator=Ada; target=alkB; function=-+
- `represses` --> [[gene.b2213|gene.b2213]] `RegulonDB` `C` - regulator=Ada; target=ada; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2213|gene.b2213]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06134`
- `KEGG:ecj:JW2201;eco:b2213;ecoc:C3026_12365;`
- `GeneID:946710;`
- `GO:GO:0003700; GO:0003908; GO:0006307; GO:0006974; GO:0008270; GO:0032259; GO:0043565; GO:0045892; GO:0045893`
- `EC:2.1.1.63; 2.1.1.n11`

## Notes

Bifunctional transcriptional activator/DNA repair enzyme Ada (Regulatory protein of adaptive response) [Includes: Methylphosphotriester-DNA--protein-cysteine S-methyltransferase (EC 2.1.1.n11) (Methylphosphotriester-DNA methyltransferase); Methylated-DNA--protein-cysteine methyltransferase (EC 2.1.1.63) (O6-methylguanine-DNA alkyltransferase)]
